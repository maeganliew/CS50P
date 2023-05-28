import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)   #reads the first row as keys
    for row in reader:   #each row returned as a dict
        students.append({"name": row['name'], "house": row['house']})   #adds a dict to the list. can straightaway students.appned(row) as row is a dict


#iterating through each dict
#lambda is like _ in looping. parameter passed in function:student, return value of function:student['name']
for student in sorted(students, key=lambda student:student['name']):
    print(f"{student['name']} is in {student['house']}")