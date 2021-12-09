# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add Modules
import csv
import os

# Load the CSV file
file_to_load = os.path.join("election Analysis/resources", "election_results.csv")

# Create file to write to
file_to_save = os.path.join("election analysis/analysis", "election_analysis.txt")

# Initialize total votes
total_votes = 0

# Create candidate options list
candidate_options = []
# Declary a candidate dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = "" # string
winning_count = 0 # integer
winning_percentage = 0 # float

# Open and read the election results file (CSV)
with open(file_to_load) as election_data:

    # Read the CSV file
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row of CSV
    for row in file_reader:
        # Add to the vote count ( += 1 is the same as var = var + 1)
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Only retrieve each candidate name once
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # track candidate votes
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate (indentation determines if its in the FOR loop or in the IF statement)
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # iterate through list
    for candidate_name in candidate_votes:
        # retrieve vote count
        votes = candidate_votes[candidate_name]
        # calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If TRUE set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate = candidate_name
            winning_candidate = candidate_name

    # print summary data
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

