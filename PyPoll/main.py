import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

with open(poll_data, "r") as csvfile:

    print("the file is open")


