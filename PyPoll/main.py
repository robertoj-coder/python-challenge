import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

with open(poll_data, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    totalVote = 0
    candidateList = []
    Votes_per_candidate = []
    
    header = next(csvreader)

    for row in csv.reader(csvfile):

        totalVote = totalVote + 1
    

        candidates = row[2]
        
        if candidates in candidateList:
            candidates_index = candidateList.index(candidates)
            Votes_per_candidate[candidates_index] = Votes_per_candidate[candidates_index] + 1

        else:

            candidateList.append(candidates)
            Votes_per_candidate.append(1)

    print(str(candidateList) + str(Votes_per_candidate))
    

    #print(candidatelist)

    print(totalVote)

    


