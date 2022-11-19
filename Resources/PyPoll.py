# The data we need to retreive
#     1 Total of the votes cast
#     2 Complete list of cadidates who received votes
#     3 Percentage of votes each candidate won
#     4 Total vote count for each candidate
#     5 winner of the election based on popular vote


# Dependencies
import os
import csv

# A variable to get the directory of executable
current_path = os.getcwd()  # current_path is of executable

# Create a variable to open the file we need
# because the .exe is in the same file, we can use this
file_to_load = os.path.join(current_path, 'election_results.csv')

# Create a filename variable to an indirect filepath to the file, wherever that is
file_to_save = os.path.join(
    current_path, "..", "Analysis", 'election_analysis.txt')
# Need to move up and then down a directory to access file, "/ .. /" Ref Ln. 8

# 1. Initialize Total vote counter
total_votes = 0

# Declare a new list for candidate options
candidate_options = []
# Declare a dictionary to hold the votes and assign them
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the results and read the data
with open(file_to_load) as election_data:  # This line initiates the CSV we're working with
    file_reader = csv.reader(election_data)
    # Read/skip the header row of csv
    headers = next(file_reader)

    # FOLLOWING RUNS THROUGH FULL CSV, THIS IS THE CORE LOOP:
    # Check each row in the CSV
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print Candidate Names
        candidate_name = row[2]

        # Add candidate name to a list if they are not already added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        # Begin tracking vote count
            # this initiates the values in the dictionary
            candidate_votes[candidate_name] = 0

        # Add a vote to the count for that candidate
        # this is aligned with the for loop, so it adds one vote per row
        candidate_votes[candidate_name] += 1

    # Save results to a text file
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n")
            
        print(election_results, end="")

        txt_file.write(election_results)

                # Determine Percentage of votes
                # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve the vote count
            votes = candidate_votes[candidate_name]

            # Calculate %
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print each candidate's name, vote count, and percentage of votes to the terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Determine winning count and candidate
            # Determine if votes is greater than winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true, set winning count to votes, win% to vote%, and name to name
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            # TO DO: MAKE THIS SAY ALL THE THINGS and also print to terminal
        winning_candidate_summary = (
            f"--------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------\n")
        # print(winning_candidate_summary)


        # Print
        # print(candidate_votes)

        # Close the file
        election_data.close()


        # Use the open statement to open the file as a text file..
        with open(file_to_save, "w") as txt_file:
            # Write some data to the file
            txt_file.write("Counties in the Election\n")
            txt_file.write("------------------------\n")
            txt_file.write("Arapahoe\nDenver\nJefferson")


        # Close the file
        txt_file.close()
