# %%
# Modules
import os
import csv
import pathlib
import pandas as pd

#Set path for file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    electiondata = pd.read_csv(csvfile)

# %%
#Find total number of votes cast by counting the rows in the dataset

total_votes = len(electiondata)

#print("Total Votes:", total_votes)

# %%
#Find a list of candidates using unique function

unique_candidates = electiondata['Candidate'].unique()

#print(unique_candidates)

# %%
#Find number of votes for each candidate and then render it as a percentage of total votes
count_stockham = (electiondata['Candidate'] == 'Charles Casper Stockham').sum()
percentage_stockham = ((count_stockham / total_votes) * 100).round(3)

count_degette = (electiondata['Candidate'] == 'Diana DeGette').sum()
percentage_degette = ((count_degette / total_votes) * 100).round(3)

count_doane = (electiondata['Candidate'] == 'Raymon Anthony Doane').sum()
percentage_doane = ((count_doane / total_votes) * 100).round(3)

# %%
#Find winner by popular vote using value_counts and idxmax

winner = electiondata['Candidate'].value_counts().idxmax()

# %%
# Print the analysis to terminal

print('Election Results')
print('----------------')
print('Total Votes:', total_votes)
print('----------------')
print('Charles Casper Stockham:', percentage_stockham, '% (', count_stockham, 'votes)')
print('Diana DeGette:', percentage_degette, '% (', count_degette, 'votes)')
print('Raymon Anthony Doane:', percentage_doane, '% (', count_doane, 'votes)')
print('----------------')
print(winner, 'won the Election')

#Save as text file.
filepath = '../analysis/output.txt'
with open(filepath, 'w') as f:
    f.write("Election Results:\n"
            "Total Votes: " + str(total_votes) + "\n"
            "Charles Casper Stockham: " + str(percentage_stockham) + "% (" + str(count_stockham) + " votes)\n"
            "Diana DeGette: " + str(percentage_degette) + "% (" + str(count_degette) + " votes)\n"
            "Raymon Anthony Doane: " + str(percentage_doane) + "% (" + str(count_doane) + " votes)\n"
            + str(winner) + " won the Election\n")

print(f"Output saved to {filepath}")

# %%



