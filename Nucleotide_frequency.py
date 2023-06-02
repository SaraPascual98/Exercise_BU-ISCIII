### Program to obtain the frequency of sequences from fasta files ###


y = -1 # loop control variable
sequence = "" # sequence container

while y == -1: 
    # Loop to repeat intro in case of error
    
    try: 
        path = input('Please, enter the path of the fasta file to analyze:' )
        with open(path, 'r') as file: 
            # Open file and read lines
            lines = file.readlines()
            
    except FileNotFoundError: 
        # Execution if the file does not exist
        print ('The path entered is invalid. Please try again')
        y = -1 

    except IsADirectoryError: # Execution if the path is a directory
        # Execution if the path is a directory
        print('The path inserted corresponds to a directory, please try again')
        y = -1
        
    except KeyboardInterrupt: 
        # Execution if press ctrl+c
        print('See you soon!')
        
    else: 
        # Run if no errors
        y = 0
        print('The chosen path is correct!')
    
        for line in lines:
        # Discard header and remove white space
            if not line.startswith('>'):
                sequence = sequence + line.rstrip()
        
        count = len(sequence) # Total number of nucleotides
                
        # Calculate the ocurrences of each nucleotide        
        G_ocurrences = sequence.count("G")
        A_ocurrences = sequence.count("A")
        C_ocurrences = sequence.count("C")
        T_ocurrences = sequence.count("T")
        N_ocurrences = sequence.count("N")
        
        # Calculate the percentage of each nucleotide
        row1 = f'The percentage of adenine in the sequences is: {A_ocurrences/count*100}%\n'
        row2 = f'The percentage of cytosine in the sequences is: {C_ocurrences/count*100}%\n'
        row3 = f'The percentage of thymine in the sequences is: {T_ocurrences/count*100}%\n'
        row4 = f'The percentage of unknown nucleotide in the sequences is: {N_ocurrences/count*100}%\n'
        
        # Print the results
        print(row1,row2,row3,row4)
        
        # Write results to a file
        with open("frequency_results.txt", "w") as results:
            results.writelines([row1,row2,row3,row4])
        
        print("The text file with the results was created successfully in the current directory !")
            
       
