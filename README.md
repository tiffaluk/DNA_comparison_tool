# DNA_comparison_tool

1. What it does:

    Given a sequence to assemble, our tool analyzes the attributes of the sequence (e.g. G-C content, presence of restriction sites, melting temperature, repeat sequences) and assigns appropriate cost penalties based on the requirements of each assembly method. Currently, the tool is able to consider 3 different assembly methods (i.e. Gibson, BioBrick, GoldenGate). At the same time, the tool does a comparative search of the best company that is capable of synthesizing the sequence (considering its different attributes) at the lowest possible cost. The user receives as a final output the best company and the best assembly method for their desired sequence. 
	
	
2. Installation:

    conda create -n newenv python
    conda activate newenv
    pip install -r requirements.txt  
        
	https://github.com/vianabar/be552-hw1.git

3. How to use:

    3.1. Preparing libraries:
        Three parts library files must be created in the form for the program to work:
            <chassis organism name>.input.json 
            <chassis organism name>.UCF.json
            <chassis organism name>.output.json

        Read https://www.nature.com/articles/s41596-021-00675-2, Supplementary Information: Section 6


    3.2. Preparing genetic circuit files:
        
        Genetic circuit files are in “.txt” form. 

        To create an input signal (example):
            gate_a = copy.deepcopy(input_signals['pTet'])
            gate_b = copy.deepcopy(input_signals['pLuxStar'])

        To create a UCF gate (example): 
            gate_c = copy.deepcopy(ucf_signals['S1_SrpR'])
        
        To create an output signal (example):
            gate_d = copy.deepcopy(output_signals['YFP'])

        To add a signal or gate to the circuit (example):
            
            c.addVertex(gate_a)
            c.addVertex(gate_b)
            c.addVertex(gate_c)
            c.addVertex(gate_d)
            
        To connect an input signal/gate to an output signal/gate in form (example):
        
            c.addEdge(gate_a,gate_c)
            c.addEdge(gate_b,gate_c)
            c.addEdge(gate_c,gate_d)

        To perform an operation on a gate/signal (example): 
            c.operate(<operation string>, x_value, gate_a)

    **Operation strings are ‘stretch’ (x <= 1.5), ‘increase_slope’ (x <= 1.05), ‘decrease_slope(x <= 1.05), ‘stronger_prom’, ‘weaker_prom’, ‘stronger RBS’, ‘weaker_RBS’



