# DNA_comparison_tool

1. What it does:

    Given a sequence to assemble, our tool analyzes the attributes of the sequence (e.g. G-C content, presence of restriction sites, melting temperature, repeat sequences) and assigns appropriate cost penalties based on the requirements of each assembly method. Currently, the tool is able to consider 3 different assembly methods (i.e. Gibson, BioBrick, GoldenGate). At the same time, the tool does a comparative search of the best company that is capable of synthesizing the sequence (considering its different attributes) at the lowest possible cost. The user receives as a final output the best company and the best assembly method for their desired sequence. 
	
	
2. Installation:

    Install Git: https://github.com/git-guides/install-git
    Install Node.js: https://nodejs.org/en/download/
    Install npm: https://docs.npmjs.com/cli/v6/commands/npm-install
	
    In terminal: 
	    git clone https://github.com/tiffaluk/DNA_comparison_tool
	    conda create -n dna_compare_env python
	    conda activate dna_compare_env
	    pip install -r requirements.txt

3. Starting Server

	After having the correct dependencies and materials as described by the equirements.txt, have 2 different terminals open. One terminal will be cd into the APISystem folder. Within said folder, run the command “python manage.py runserver” which will start the Django server and connect to the MongoDB Atlas database. In a different terminal, cd into the dna-tool server and run the command “npm start” which will start the react.js server and run the react app in development mode.

4. Using the website
	When the user enters the front page, they are able to press the "Assembly my Sequence!" button which leads them to the order sites. After inputing their sequence, they are able to choose between dsDNA,ssDNA, RNA, and Amino Acids based on their choice. After pressing submit, our database will give them the best possible company and also the best assembly method with the turnaround time and cost. The user can press company details to learn more about how each company calculate the price or assembly details to learn about how each assemly method was calculated
