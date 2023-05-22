students = ["hermione", "harry", "ron"]

for s in students:
    print(s)

for i in range(len(students)):
    print(students[i])



#dictionaries
dict_students = {"hermione": "gryffindor",
                 "harry": "gryffindor",
                 "draco": "slytherin "}

for p in dict_students:    #iterates every key. p is a key
    print(p, dict_students[p], sep=": ")



#list of dictionaries
stu = [
    {"name":"hermione", "house":"gryffindor", "patronus":"otter"},
    {"name":"draco", "house":"slytherin", "patronus":None}  #None is a key-word in python, represents the absence of value
]

for people in stu:  #iterating over list of dictionaries
    print(people["name"])