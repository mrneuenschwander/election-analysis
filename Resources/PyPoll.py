# The data we need to retreive

#Dependencies
import os
import csv
dir(csv)

#A variable to get the directory of executable
current_path = os.getcwd() #current_path is of executable

#Create a variable to open the file we need
file_to_load = os.path.join(current_path, 'election_results.csv') #because the .exe is in the same file, we can use this
#Create a filename variable to an indirect filepath to the file
file_to_save = os.path.join(current_path, "..", "Analysis", 'election_analysis.txt')
    #Need to move up and then down a directory to access file, "/ .. /" Ref Ln. 8

#Open the results and read the data
with open(file_to_load) as election_data:
    
    # TO DO: Perform analysis
    file_reader = csv.reader(election_data)
    #Read and print the header row of csv
    headers = next(file_reader)
    print(headers)
    
    #FOLLOWING PRINTS FULL CSV:
    # for row in file_reader:
    #     print(row)
    
#Close the file
    election_data.close()


# Use the open statement to open the file as a text file..
with open(file_to_save, "w") as txt_file:
    #Write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


#Close the file
txt_file.close()

#     1 Total of the votes cast
#     2 Complete list of cadidates who received votes
#     3 Percentage of votes each candidate won
#     4 Total vote count for each candidate
#     5 winner of the election based on popular vote