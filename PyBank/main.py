import os
import csv

#path the collected data from the resources folder
#dirname = os.path.dirname(__file__)
budget_path = os.path.join("Resources", "budget_data.csv")
 
#open the CSV
with open(budget_path, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
   
  
  
    #Reset value to 0 to calculate total profit(totalP)and number of months
    F1 = []
    monthAverage = []
    totalP = 0
    months = 0
# eliminate the header from the file
    header = next(csvreader)
#loop through looking for bufget and dates
    for row in csv.reader(csvfile):
        
        F1.append(int(row[1]))
        monthAverage.append(row[0])
#calculate the total profit and the number of months
        totalP = totalP + (int(row[1]))
        months = months + 1


        profit_change = []

        for i in range(1, len(F1)):
# calculate the changes in profit/losses oveer the entire period
            profit_change.append((int(F1[i]) - int(F1[i-1]))) 
            average_change = sum(profit_change) / len(profit_change)
 #calculate the greatest increase and decrease of the profit change             
            increase = max(profit_change)
            decrease = min(profit_change)

# Print the results           
print("Financial Analysis")

print("-"*30)

print("Total months: " + str(months))
print("Total volume: " "$"  +  str(totalP))
print("Average Change:" + "$"  +  str(round(average_change, 2)))
print("Greatest Increase in profit:" + str(monthAverage[profit_change.index(max(profit_change))+1]) + " " + "$"+ str(increase))
print("Greatest Decrease in profit:" + str(monthAverage[profit_change.index(min(profit_change))+1]) + " " + "$"+ str(decrease))

# Output a text file

text_file = open("output.txt", "w")
text_file.write("Financial Analysis" + "\n")

text_file.write("-------------------------------" + "\n")

text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: " "$"  +  str(totalP) + "\n")
text_file.write("Average Change:" + "$"  +  str(round(average_change, 2)) + "\n")
text_file.write("Greatest Increase in profit:" + str(monthAverage[profit_change.index(max(profit_change))+1]) + " " + "$"+ str(increase) + "\n")
text_file.write("Greatest Decrease in profit:" + str(monthAverage[profit_change.index(min(profit_change))+1]) + " " + "$"+ str(decrease) + "\n")

text_file.close()

 






