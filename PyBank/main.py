import os
import csv


budget_path = os.path.join("Resources", "budget_data.csv")
print(budget_path)

""" with open(budget_path, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reset value to 0 to calculate total profit(totalP)and number of months
    totalP = 0
    months = 0

    header = next(csvreader)

    for row in csv.reader(csvfile):

        totalP = totalP + (int(row[1]))
        months = months + 1

print("Total months: " + str(months))
print("Total volume: " + str(totalP))

 """


        


 






