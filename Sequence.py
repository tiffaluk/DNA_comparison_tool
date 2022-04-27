from Bio.Blast import NCBIWWW
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Sequence class for input genetic sequences
class Sequence:
    def	__init__(self, name, num_strands):
        self.name = name.upper()
        self.assembly_cost = []
        self.company_cost = []
        self.turn_time = 0
        self.gc_content = self.get_gc_content()
        self.num_strands = num_strands
        self.tm = -273.15 #sequence melting point
        
        self.fold_score = 0
        self.parts = []
        
        
    def get_gc_content(self):
        c_content = self.name.count('C')
        g_content = self.name.count('G')
        self.gc_content = (c_content + g_content) / len(self.name)

    def get_melting_temp(self):
        a_content = self.name.count('A')
        t_content = self.name.count('T')
        c_content = self.name.count('C')
        g_content = self.name.count('G')
        self.tm = 2*(a_content + t_content) + 4*(c_content + g_content) - 7

    def get_folding_score(self):
        analyzed_seq = ProteinAnalysis(self.name)
        helix_perc, turn_perc, sheet_perc = analyzed_seq.secondary_structure_fraction()

        self.fold_score = helix_perc + turn_perc + sheet_perc
        

    
