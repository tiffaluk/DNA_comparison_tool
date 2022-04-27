import pandas as pd
import numpy as np
import os

from hashlib import new
from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Sequence class for input genetic sequences
class Sequence:
    def	__init__(self, name, type):
        self.name = name.upper()
        self.type = type

        self.turn_time = 0
        self.gc_content = 0
        self.get_gc_content()

        self.tm = -273.15 #sequence melting point
        self.get_melting_temp()

        self.fold_score = 0
        self.get_folding_score()

        self.bb_parts = []
        self.gg_parts = []

        #0 is, 1 is biobrick, 2 is, 3 is goldengate, 4 is
        self.assembly_cost = [float('inf')] * 5
        self.company_cost = [float('inf')] * 5

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

        ecori_site = "AATTC"
        xbal_site = "CTAGA"
        spel_site = "CTAGT"
        pstl_site = "CTGCA"

        res_sites = [ecori_site,xbal_site,spel_site,pstl_site]

        if any(res_site in self.name for res_site in res_sites):
            cost_penalty = float('inf')

        self.get_bb_parts()

        self.assembly_cost[1] = cost_penalty

    def check_gg(self):
        cost_penalty = 0

        bsal_site_5 = "GGTCTC"

        segment = self.name

        if bsal_site_5 in segment:
            cost_penalty = float('inf')

        if self.tm < 37:
            cost_penalty = float('inf')

        
        self.gg_parts.append(self.name)
        self.get_gg_parts()

        self.assembly_cost[3] = cost_penalty

    # Split desired dna sequence into possible parts for assembly
    def get_bb_parts(self):
        biobrick_df = pd.read_csv('biobrick_library.csv')
        bb_lib_np = biobrick_df.to_numpy()
        print(bb_lib_np)


    def get_gg_parts(self):
        if len(max(self.gg_parts, key=len)) <= 100: # don't have to split after 1000
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

    



