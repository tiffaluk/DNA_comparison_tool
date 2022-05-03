import pandas as pd
import numpy as np
import os
import random
import re


from hashlib import new
from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Sequence class for input genetic sequences
class Sequence:
    def	__init__(self, name, type):
        self.name = name.upper()
        if type == 'ssDNA' or type == 'dsDNA':
            self.name = name
        elif type == 'RNA':
            self.name = name.replace("U", "T")
        elif type == 'Amino Acids':

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

        # hours to days for turn time
        for i in range(len(self.turn_time)):
            self.turn_time[i] = self.turn_time[i] / 24

    # Get GC content of sequence
    def get_gc_content(self):
        c_content = self.name.count('C')
        g_content = self.name.count('G')
        self.gc_content = (c_content + g_content) / len(self.name)

    # get melting temperature of sequence
    def get_melting_temp(self):
        self.tm = MeltingTemp.Tm_NN(Seq(self.name))

    # Return proportion of sequence which will likely fold into
    # Secondary structure
    def get_folding_score(self):
        analyzed_seq = ProteinAnalysis(self.name)
        helix_perc, turn_perc, sheet_perc = analyzed_seq.secondary_structure_fraction()

        self.fold_score = helix_perc + turn_perc + sheet_perc

    # Check if assembly method is possible for sequence for
    # biobrick, golden gate, and gibson
    def check_bb(self):


        self.get_bb_parts()

        # 6 hour penalty for joining two biobrick parts
        self.turn_time[0] = (len(self.bb_parts) - 1) * 6

    def check_gg(self):

        bsal_site_5 = "GGTCTC"

        segment = self.name

        # if violating recognition site is in sequence,
        # golden gate assembly doesnt work
        if bsal_site_5 in segment:
            self.assembly_cost[1] = float('inf')
            self.turn_time[1] = float('inf')
            return

        # golden gate assembly doesnt work if sequence has
        # melting temp < 37degC
        if self.tm < 37:
            self.assembly_cost[1] = float('inf')
            self.turn_time[1] = float('inf')
            return


        self.gg_parts.append(self.name)
        self.get_gg_parts()

        # turn time penalty of 55 hours for golden gate assembly
        self.turn_time[1] = 55

        # charge extra for dna synthesis of remnants from scratch ($0.1 per bp), add time
        # penalty of 1 hr for dna synthesis of each part from scratch
        for curr_part in self.gg_parts:
            self.turn_time[1] = self.turn_time[2] + 1
            self.assembly_cost[1] = self.assembly_cost[2] + 0.1 * len(curr_part)
        # Cost penalty of $3 per part joining
        self.assembly_cost[1] = self.assembly_cost[1] + 3 * len(self.gg_parts)

    def check_gibson(self):
        self.get_gibson_parts()





    # Split desired dna sequence into possible parts for assembly for
    # biobrick, golden gate, and gibson
    def get_bb_parts(self):
        # Read biobrick parts from standard 10 biobrick library
        total_seq = self.name
        biobrick_df = pd.read_csv('biobrick_library.csv')
        bb_lib_np = biobrick_df.to_numpy()

        # find out whether sequence contains biobrick parts, if so
        # add to bb_parts for sequence
        count = 0
        for i in range(len(bb_lib_np)):
            for match in re.finditer(bb_lib_np[i][1], total_seq):
                print(bb_lib_np[i][1])
                self.bb_parts.append(bb_lib_np[i][1])
                s = match.start()
                e = match.end()
                for i in range(s, e):
                    total_seq = total_seq[:i] + "_" + total_seq[i+1:]

        # if part exists in the biobrick library, then assembly cost is $2.50 per part
        self.assembly_cost[0] = self.assembly_cost[0] + len(self.bb_parts) * 2.50

        # find remnants of sequence and join to bb_parts of sequence
        total_seq_remain = total_seq.split("_")
        total_seq_remain = ' '.join(total_seq_remain).split()
        self.bb_parts.extend(total_seq_remain)

        # if illegal patterns exist in custom dna remnants, make biobrick
        # prohibited
        ecori_site = "AATTC"
        xbal_site = "CTAGA"
        spel_site = "CTAGT"
        pstl_site = "CTGCA"
        res_sites = [ecori_site,xbal_site,spel_site,pstl_site]

        # charge extra for dna synthesis of remnants from scratch ($0.1 per bp), add time
        # penalty of 1 hr for dna synthesis of each part from scratch

        for curr_part in total_seq_remain:

            if any(res_site in curr_part for res_site in res_sites):
                self.assembly_cost[0] = float('inf')
                self.turn_time[0]= float('inf')
                return

            self.turn_time[2] = self.turn_time[2] + 1
            self.assembly_cost[2] = self.assembly_cost[2] + 0.1 * len(curr_part)

        count = count + len(total_seq_remain)


    def get_gg_parts(self):
        # don't have to split after part is < 100 bp
        if len(max(self.gg_parts, key=len)) <= 100:
            return
        else:
            old_max_len = len(max(self.gg_parts, key=len))
            new_gg_parts = []

            # split each part into 2 subparts of half size
            for gg_part in self.gg_parts:
                gg_half_1, gg_half_2 = gg_part[:len(gg_part)//2], gg_part[len(gg_part)//2:]

                # if subpart is less than minimum part size, join subparts
                # back together to prevent violation of golden gate
                if len(gg_half_2) < 22: #22 is minimum part size
                    new_gg_parts.append(str(gg_half_1 + gg_half_2))
                else:
                    new_gg_parts.append(gg_half_1)
                    new_gg_parts.append(gg_half_2)

            self.gg_parts = new_gg_parts
            new_gg_parts = []

            # if overhang violation exists between parts, join parts together
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
        size_range = range(500, 32000)

        # assign number of parts allowed based on
        # length of sequence
        if len(self.name) < 500:
            self.turn_time[2] = float('inf')
            self.assembly_cost[2] = float('inf')
            return
        elif len(self.name) < 1000:
            self.gibson_parts = self.name
            self.turn_time[2] = 1 * len(self.name)
            self.assembly_cost[2] = 0.01 * len(self.name)
            return
        elif len(self.name) < 1500:
            num_parts = 2
        elif len(self.name) < 2000:
            num_parts = 3
        elif len(self.name) < 2500:
            num_parts = 4
        elif len(self.name < 32000):
            num_parts = 5

        # randomly split sequence into parts of different sizes,
        # pick best set of parts based on least amount of secondary
        # structure
        best_parts = []
        best_sec_struct_score = float('inf')
        for i in range(100):
            curr_parts = []
            curr_point = 0
            for j in range(num_parts-1):
                random_point = random.randint(500, len(self.name) // num_parts)
                curr_parts.append(self.name[curr_point:curr_point + random_point])
                curr_point = curr_point + random_point

            curr_parts.append(self.name[curr_point:])

            new_curr_parts = []
            if len(curr_parts) > 1:
                seen = dict()
                for i in range(len(curr_parts)):
                    overhang = curr_parts[i][0:40]
                    if overhang in seen:
                        new_curr_parts[-1] = new_curr_parts[-1] + str(curr_parts[i])
                    else:
                        new_curr_parts.append(curr_parts[i])
                        seen[overhang] = i
            curr_parts = new_curr_parts

            temp_fail = 0
            sec_struct_score = 0
            for curr_part in curr_parts:
                # don't allow parts to be created for gibson if
                # their melting temperatures are < 50 (creates
                # complications for gibson)
                if MeltingTemp.Tm_Wallace(Seq(curr_part)) < 50:
                    temp_fail = 1
                    break
                else:
                    analyzed_curr_part = ProteinAnalysis(curr_part)
                    helix_perc, turn_perc, sheet_perc = analyzed_curr_part.secondary_structure_fraction()
                    sec_struct_score = sec_struct_score + helix_perc + turn_perc + sheet_perc

            if len(best_parts) == 0 and temp_fail == 0:
                best_parts = curr_parts
            elif sec_struct_score < best_sec_struct_score and temp_fail == 0:
                best_parts = curr_parts

        self.gibson_parts = best_parts

        if len(self.gibson_parts) == 0:
            self.turn_time = float('inf')
            self.assembly_cost[2] = float('inf')
            return

        # 1-stage gibson assembly has time penalty of 80 hours
        self.turn_time[2] = 80

        # cost penalty for increasing difficulties if secondary structures
        # are more prevalent
        self.assembly_cost[2] = self.assembly_cost[2] + 0.01 * best_sec_struct_score

        # charge extra for dna synthesis of remnants from scratch ($0.1 per bp), add time
        # penalty of 1 hr for dna synthesis of each part from scratch
        for curr_part in self.gibson_parts:
            self.turn_time[2] = self.turn_time[2] + 1
            self.assembly_cost[2] = self.assembly_cost[2] + 0.1 * len(curr_part)




    # return best assembly method, its cost, and its turnaround time
    def get_best_assembly_method(self):
        min_assembly_cost = min(self.assembly_cost)
        min_assembly_index = self.assembly_cost.index(min_assembly_cost)

        min_turn_time = min(self.turn_time)
        min_turn_index = self.turn_time.index(min_turn_time)
        if min_assembly_index == 0:
            assembly_method = "BioBrick"
        elif min_assembly_index == 1:
            assembly_method = "GoldenGate"
        elif min_assembly_index == 2:
            assembly_method = "Gibson"

        return assembly_method, min_assembly_cost, self.turn_time[min_assembly_index]
