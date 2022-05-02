import pandas as pd
import numpy as np
import os
import re

from hashlib import new
from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Sequence class for input genetic sequences
class Sequence:
    def	__init__(self, name, type):
        name = name.upper()
        if type == 'ssDNA' or type == 'dsDNA':
            self.name = name
        elif type == 'RNA':
            self.name = name.replace("U", "T")
        elif type == 'AA':

            prot_table = {
                'A': 'GCA',
                'C': 'TGC',
                'D': 'GAC',
                'E': 'GAA',
                'F': 'TTC',
                'G': 'GGA',
                'H': 'CAC',
                'I': 'ATA',
                'K': 'AAA',
                'L': 'CTA',
                'M': 'ATG',
                'N': 'AAC',
                'P': 'CCA',
                'Q': 'CAA',
                'R': 'AGA',
                'S': 'AGC',
                'T': 'ACA',
                'V': 'GTA',
                'W': 'TGG',
                'Y': 'TAC',
                '_': 'TAA',
                }
            self.name = ""
            for i in range(len(name)):
                self.name += prot_table[name[i]]

        self.type = type


        self.gc_content = 0
        self.get_gc_content()

        self.tm = -273.15 #sequence melting point
        self.get_melting_temp()

        self.fold_score = 0
        self.get_folding_score()

        self.bb_parts = []
        self.gg_parts = []
        self.gibson_parts = []

        #0 is biobrick, 1 is goldengate, 2 is gibson
        self.turn_time = [0,0,0]
        self.assembly_cost = [0,0,0]
        self.company_cost = [0,0,0]

        self.check_bb()
        self.check_gg()
        self.check_gibson()

    # Get basic sequence characteristics
    def get_gc_content(self):
        c_content = self.name.count('C')
        g_content = self.name.count('G')
        self.gc_content = (c_content + g_content) / len(self.name)

    def get_melting_temp(self):
        self.tm = MeltingTemp.Tm_Wallace(Seq(self.name))

    def get_folding_score(self):
        analyzed_seq = ProteinAnalysis(self.name)
        helix_perc, turn_perc, sheet_perc = analyzed_seq.secondary_structure_fraction()

        self.fold_score = helix_perc + turn_perc + sheet_perc

    # Check if assembly method is possible for sequence
    def check_bb(self):
        cost_penalty = 0
        '''
        ecori_site = "AATTC"
        xbal_site = "CTAGA"
        spel_site = "CTAGT"
        pstl_site = "CTGCA"

        res_sites = [ecori_site,xbal_site,spel_site,pstl_site]

        if any(res_site in self.name for res_site in res_sites):
            self.assembly_cost[0] = float('inf')
            self.turn_time[0]= float('inf')
            return
        '''
        self.get_bb_parts()

        self.turn_time[0] = (len(self.bb_parts) - 1) * 30
        self.assembly_cost[0] = cost_penalty

    def check_gg(self):
        cost_penalty = 0

        bsal_site_5 = "GGTCTC"

        segment = self.name

        if bsal_site_5 in segment:
            self.assembly_cost[1] = float('inf')
            self.turn_time[1] = float('inf')
            return

        if self.tm < 37:
            self.assembly_cost[1] = float('inf')
            self.turn_time[1] = float('inf')
            return


        self.gg_parts.append(self.name)
        self.get_gg_parts()

        cost_penalty = cost_penalty + len(self.gg_parts) * 2

        self.assembly_cost[1] = cost_penalty
        self.turn_time[1] = 30 * len(self.gg_parts) + 30

    def check_gibson(self):
        self.get_gibson_parts()

        if self.tm < 50:
            self.assembly_cost[2] = self.assembly_cost[2] + 30
            self.turn_time[2] = self.turn_time[2] + 30



    # Split desired dna sequence into possible parts for assembly
    def get_bb_parts(self):
        total_seq = self.name
        biobrick_df = pd.read_csv('biobrick_library.csv')
        bb_lib_np = biobrick_df.to_numpy()

        count = 0
        for i in range(len(bb_lib_np)):
            for match in re.finditer(bb_lib_np[i][1], total_seq):
                print(bb_lib_np[i][1])
                self.bb_parts.append(bb_lib_np[i][1])
                s = match.start()
                e = match.end()
                for i in range(s, e):
                    total_seq = total_seq[:i] + "_" + total_seq[i+1:]

        self.assembly_cost[0] = self.assembly_cost[0] + len(self.bb_parts) * 5

        total_seq_remain = total_seq.split("_")
        total_seq_remain = ' '.join(total_seq_remain).split()
        self.bb_parts.extend(total_seq_remain)

        self.assembly_cost[0] = self.assembly_cost[0] + len(total_seq_remain) * 30
        self.turn_time[0] = self.turn_time[0] + 30*len(total_seq_remain)

        count = count + len(total_seq_remain)


    def get_gg_parts(self):
        if len(max(self.gg_parts, key=len)) <= 100: # don't have to split after 100
            return
        else:
            old_max_len = len(max(self.gg_parts, key=len))
            new_gg_parts = []
            for gg_part in self.gg_parts:
                gg_half_1, gg_half_2 = gg_part[:len(gg_part)//2], gg_part[len(gg_part)//2:]

                if len(gg_half_2) < 22: #22 is minimum part size
                    new_gg_parts.append(str(gg_half_1 + gg_half_2))
                else:
                    new_gg_parts.append(gg_half_1)
                    new_gg_parts.append(gg_half_2)

            self.gg_parts = new_gg_parts
            new_gg_parts = []

            if len(self.gg_parts) > 1:
                seen = dict()
                for i in range(len(self.gg_parts)):
                    overhang = self.gg_parts[i][0:4]
                    if overhang in seen:
                        new_gg_parts[-1] = new_gg_parts[-1] + str(self.gg_parts[i])
                    else:
                        new_gg_parts.append(self.gg_parts[i])
                        seen[overhang] = i

            self.gg_parts = new_gg_parts
            new_max_len = len(max(self.gg_parts, key=len))
            if new_max_len < old_max_len:
                self.get_gg_parts()
            else:
                return

    def get_gibson_parts(self):
        #parts can be 500 bp to 32 kb long
        num_parts = 5

        '''
        if len(self.name) < 500:
            self.turn_time = float('inf')
            self.assembly_cost = float('inf')
        elif len(self.name) < 1000:
            self.gibson_parts = self.name
            self.turn_time = 30
            self.assembly_cost
        elif len(self.name) < 1500:
            num_parts =
        '''

        self.gibson_parts = [self.name[i:i+num_parts] for i in range(0, len(self.name), num_parts)]
        self.turn_time[2] = 80 + 30 * len(self.gibson_parts)

        self.turn_time[2] = 80
        self.assembly_cost[2] = 30*len(self.gibson_parts)




    def get_best_assembly_method(self):
        min_assembly_cost = min(self.assembly_cost)
        min_assembly_index = self.assembly_cost.index(min_assembly_cost)

        #min_turn_time = min(self.turn_time)
        #min_turn_index = self.turn_time.index(min_turn_time)
        assembly_method_index=1
        assembly_method=""
        if min_assembly_index == 0:
            assembly_method = "BioBrick"
        elif min_assembly_index == 1:
            assembly_method = "GoldenGate"
        elif min_assembly_index == 2:
            assembly_method = "Gibson"

        return assembly_method, min_assembly_cost
