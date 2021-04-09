import csv
import os
cwkdir = os.getcwd()
path = os.path.join(cwkdir, "Resources", "election_data.csv")
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
max_votes = 0
def percentage (part, whole):
    return 100 * float(part)/float(whole)
with open(path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for i in csvreader:
            voterid = i[0]
            country = i[1]
            candidate = i[2]
            total_votes = total_votes + 1
            if candidate =="Khan":
                khan_votes = khan_votes + 1
            if candidate =="Correy":
                correy_votes = correy_votes + 1
            if candidate =="Li":
                li_votes = li_votes + 1
            if candidate =="O'Tooley":
                otooley_votes = otooley_votes + 1
        candidate_total = {"Khan": khan_votes,"Correy": correy_votes,"Li": li_votes,"O'Tooley": otooley_votes}
        for candidate, value in candidate_total.items():
            if value > max_votes:
                max_votes = value
                winner = candidate
print(f'Election Results'+'\n')
print(f'--------------------'+'\n')
print(f'Total Votes: {total_votes}'+'\n')
print(f'--------------------'+'\n')
print(f'Khan: {percentage(khan_votes,total_votes):.3f}% ({khan_votes})')
print(f'Correy: {percentage(correy_votes,total_votes):.3f}% ({correy_votes})')
print(f'Li: {percentage(li_votes,total_votes):.3f}% ({li_votes})')
print(f'O\'Tooley: {percentage(otooley_votes,total_votes):.3f}% ({otooley_votes})')
print(f'--------------------'+'\n')
print(f'Winner: {winner} '+'\n')