import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")
#open the CSV
with open(poll_data, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
#declaring variables for total votes and creating dictionary for candidates
    totalVote = 0
    candidateDict = {}
   
    
    header = next(csvreader)
#Looping to count votes
    for row in csvreader:
#calculating total votes
        totalVote = totalVote + 1
    
#Establishing candidate row
        candidate = row[2]
        
       # if candidates not in candidateList:
        if candidate in candidateDict.keys():
           # candidate in the dictionary 
           candidateDict[candidate] += 1
           
        else:
           #candidate not yet in dictionary
         
           candidateDict[candidate] = 1
           
#printing the total vote          
print("Election Results")
print("-"*30)

print("Total Vote:" + str(totalVote))

print("-"*30)
# setting variable to zero
winning_count = 0

for entry in candidateDict:

#printing list of candidates , calculating percentages, and printing votes per candidates
   print(f"{entry}:  {round(candidateDict[entry]/totalVote*100, 3)} % ({candidateDict[entry]})")
# Determine the winner
   if candidateDict[entry] > winning_count:
      winning_count = candidateDict[entry]
      winner = entry  
print("-"*30)
print("winner:" + "  "+ winner)



# Output a text file
text_file = open("output.txt", "w")
text_file.write("Election Results" + "\n")

text_file.write("-------------------------" + "\n")
text_file.write("Total Vote:" + str(totalVote) + "\n")

text_file.write("-------------------------" + "\n")
for entry in candidateDict:
   text_file.write(f"{entry}:  {round(candidateDict[entry]/totalVote*100, 3)} % ({candidateDict[entry]}) \n")

text_file.write("-------------------------" + "\n")
text_file.write("winner:" + "  "+ winner)  
text_file.close()


    
