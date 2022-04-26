# Sequence class for input genetic sequences
class Sequence:
    def	__init__(self, name, num_strands):
        self.name = name
        self.cost = 0
        self.turn_time = 0
        self.gc_content = 0
        self.num_strands = num_strands
        
        self.fold_score = 0
        self.
        
        if self.gate_type != 'Output':
            self.calculate_truth_table()
            self.calculate_score()
            