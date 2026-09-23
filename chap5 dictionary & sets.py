# DICTIONARY:

# Dictionary: Python dictionary is a collection used to store data in key-value pairs.

student = {"name":"Shivam","age":18,"branch":"CSE"}

print(student)
# OUTPUT={'name': 'Shivam', 'age': 18, 'branch': 'CSE'}

# 1: ACCESSING DICTIONARY:

# Dictionary me value ko key ke through access karte hain.

student = {"name":"Shivam","age":18,"branch":"CSE"}

print(student["name"])     # OUTPUT=Shivam
print(student["age"])      # OUTPUT=18
print(student["branch"])   # OUTPUT=CSE

# 2: DICTIONARY IS MUTABLE:

# Dictionary mutable hoti hai, iska matlab dictionary ki values ko change kar sakte hain.

student = {"name":"Shivam","age":18}

student["age"] = 19

print(student)
# OUTPUT={'name': 'Shivam', 'age': 19}

# 3: ADDING NEW ITEM:

# Dictionary me new key-value pair add kar sakte hain.

student = {"name":"Shivam","age":18}

student["branch"] = "CSE"

print(student)
# OUTPUT={'name': 'Shivam', 'age': 18, 'branch': 'CSE'}

# 4: DELETE ITEM:

# Dictionary se item delete karne ke liye del use kar sakte hain.

student = {"name":"Shivam","age":18,"branch":"CSE"}

del student["age"]

print(student)
# OUTPUT={'name': 'Shivam', 'branch': 'CSE'}

# DICTIONARY PROPERTIES:
# 1. Dictionary key-value pairs me data store karti hai
# 2. Dictionary mutable hoti hai
# 3. Dictionary me keys unique hoti hain
# 4. Dictionary me duplicate values ho sakti hain
# 5. Dictionary different data types ki values store kar sakti hai
# 6. Dictionary {} curly brackets use karti hai
# 7. Dictionary ko key ke through access karte hain
# DICTIONARY SYNTAX:
# dictionary = {
#     "key1":"value1",
#     "key2":"value2"
# }

# DICTIONARY METHODS:
# | Method    | Kaam                              | Example              |
# |-----------|-----------------------------------|-----------------------|
# | keys()    | Saari keys deta hai               | student.keys()        |
# | values()  | Saari values deta hai             | student.values()      |
# | items()   | Key aur value dono deta hai       | student.items()       |
# | get()     | Key ki value deta hai             | student.get("name")   |
# | update()  | Item add/change karta hai          | student.update(...)   |
# | pop()     | Specific item remove karta hai    | student.pop("age")    |
# | clear()   | Dictionary empty karta hai         | student.clear()       |
# | copy()    | Dictionary ki copy banata hai     | student.copy(