# Chapter 9 challenges

""" write the list items to a csv file """
fp = "chap9_movies.csv"
lst1 = [
    "Top Gun",
    "Risky Businsess",
    "Minority Report",
    ]
lst2 = [
    "Titanic",
    "The Revenant",
    "Inception",
    ]
lst3 = [
    "Training Day",
    "Man on Fire",
    "Flight"
    ]
movies = [lst1, lst2, lst3]
import csv
with open(fp, "w") as f: # open file for writing and close when finished
    w = csv.writer(f, delimiter=",") # create a csv write object
    for lst in movies:
        w.writerow(lst) # use csv writer object's writerow method to write a new row to .csv file

print("Retrieving movie list... \n")

with open(fp, "r") as f: # open file for reading and close when finished
    r = csv.reader(f, delimiter=",") # create a csv reader object
    for row in r:
        print(",".join(row)) # use str.join method to add comma between each piece of data in file
