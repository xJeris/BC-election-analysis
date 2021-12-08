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

# Open and read the election results file (CSV)
with open(file_to_load) as election_data:

    # Read the CSV file
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

