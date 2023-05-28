import csv

name = input("Whats your name? ")
house = input("What's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])   #fieldnames is like specifying the columns inside file
    writer.writerow({"name": name, "house": house})