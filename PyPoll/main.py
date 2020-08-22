import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

with open(poll_data, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    totalVote = 0
    candidateDict = {}
    #Votes_per_candidate = []
    
    header = next(csvreader)

    for row in csvreader:

        totalVote = totalVote + 1
    

        candidate = row[2]
        
       # if candidates not in candidateList:
        if candidate in candidateDict.keys():
           # candidate in the dictionary 
           #candidateDict[candidate] = candidateDict[candidate] + 1
           candidateDict[candidate] += 1
           #candidateList.append(candidates)
           #Votes_per_candidate.append(candidateList)
           #Votes_per_candidate[candidateList] = Votes_per_candidate[candidateList] + 1
          # candidates_index = candidateList.index(candidates)
           #candidates_index = candidateList.index(candidates)
           #Votes_per_candidate[candidates_index] = Votes_per_candidate[candidates_index] + 1
        else:
           #candidate not yet in dictionary
           #candidateList.append(candidates)
           candidateDict[candidate] = 1
           #Votes_per_candidate.append(1)
           

           
winning_count = 0

for entry in candidateDict:


   print(f"{entry}:  {round(candidateDict[entry]/totalVote*100, 3)} % ({candidateDict[entry]})")
   if candidateDict[entry] > winning_count:
      winning_count = candidateDict[entry]
      winner = entry  

print("winner:" + "  "+ winner)


# Output a text file
text_file = open("output.txt", "w")
text_file.write("Election Results" + "\n")

text_file.write("-------------------------" + "\n")
text_file.write(f"{entry}:  {round(candidateDict[entry]/totalVote*100, 3)} % ({candidateDict[entry]})" +"\n")

text_file.write("-------------------------" + "\n")
text_file.write("winner:" + "  "+ winner)  

    
