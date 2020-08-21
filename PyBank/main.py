import os
import csv


#dirname = os.path.dirname(__file__)
budget_path = os.path.join("Resources", "budget_data.csv")
 

with open(budget_path, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
   
  
  
    #Reset value to 0 to calculate total profit(totalP)and number of months
    F1 = []
    monthAverage = []
    totalP = 0
    months = 0

    header = next(csvreader)

    for row in csv.reader(csvfile):
        
        F1.append(int(row[1]))
        monthAverage.append(row[0])
        totalP = totalP + (int(row[1]))
        months = months + 1


        profit_change = []

        for i in range(1, len(F1)):
            profit_change.append((int(F1[i]) - int(F1[i-1]))) 
            average_change = sum(profit_change) / len(profit_change)
              
            increase = max(profit_change)
            decrease = min(profit_change)


print("Total months: " + str(months))
print("Total volume: " + str(totalP))
print("Average Change:" + str(round(average_change, 2)))
print("Greatest Increase in profit:" +   str(increase))
print("Greatest Decrease in profit:" +   str(decrease))





 






