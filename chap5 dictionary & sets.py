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

# DICTIONARY METHODS & OPERATIONS:
    
# Method / Operation	Kaam /	Example 
# keys()	Saari keys deta hai.	student.keys()
# values()	Saari values deta hai.	student.values()
# items()	Key aur value dono deta hai.	student.items()
# get()	Key ki value deta hai.	student.get("name")
# update()	Item add/change karta hai.	student.update(...)
# pop()	Specific key ko remove karta hai.	student.pop("age")
# popitem()	Last key-value pair remove karta hai.	student.popitem()
# clear()	Dictionary empty karta hai.	student.clear()
# copy()	Dictionary ki copy banata hai.	student.copy()
# setdefault()	Key nahi hai to add karta hai.	student.setdefault(...)
# fromkeys()	Given keys se new dictionary banata hai.	dict.fromkeys(...)
# len()	Total key-value pairs count karta hai.	len(student)
# del	Specific key-value pair delete karta hai.	del student["age"] 

# keys():
# keys() dictionary ki saari keys deta hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print(student.keys())
# OUTPUT=dict_keys(['name', 'age', 'branch'])


# values():
# values() dictionary ki saari values deta hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print(student.values())
# OUTPUT=dict_values(['Shivam', 18, 'CSE'])


# items():
# items() dictionary ki key aur value dono deta hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print(student.items())
# OUTPUT=dict_items([('name', 'Shivam'), ('age', 18), ('branch', 'CSE')])


# get():
# get() kisi key ki value ko access karne ke liye use hota hai.

student = {"name":"Shivam","age":18}
print(student.get("name"))
# OUTPUT=Shivam


# Agar key dictionary me nahi hai to get() normally None return karta hai.

student = {"name":"Shivam","age":18}
print(student.get("marks"))
# OUTPUT=None


# update():
# update() dictionary me new item add ya existing value change karne ke liye use hota hai.

student = {"name":"Shivam","age":18}
student.update({"age":19})
print(student)
# OUTPUT={'name': 'Shivam', 'age': 19}


# New item bhi add kar sakte hain:

student.update({"branch":"CSE"})
print(student)
# OUTPUT={'name': 'Shivam', 'age': 19, 'branch


# pop():
# pop() specified key aur uski value ko dictionary se remove karta hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
student.pop("age")
print(student)
# OUTPUT={'name': 'Shivam', 'branch': 'CSE'}


# clear():
# clear() dictionary ke saare items remove kar deta hai.

student = {"name":"Shivam","age":18}
student.clear()
print(student)
# OUTPUT={}


# copy():
# copy() dictionary ki ek copy banata hai.

student = {"name":"Shivam","age":18}
new_student = student.copy()
print(new_student)
# OUTPUT={'name': 'Shivam', 'age': 18}


# len():
# len() dictionary me total key-value pairs ki number batata hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print(len(student))
# OUTPUT=3


# IN:
# in check karta hai ki koi key dictionary ke andar present hai ya nahi.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print("name" in student)
# OUTPUT=True

print("marks" in student)
# OUTPUT=False


# NOT IN:
# not in check karta hai ki key dictionary ke andar present nahi hai.

student = {"name":"Shivam","age":18,"branch":"CSE"}
print("marks" not in student)
# OUTPUT=True

print("name" not in student)
# OUTPUT=False


# DICTIONARY LOOP:
# Dictionary par for loop laga sakte hain.

student = {"name":"Shivam","age":18,"branch":"CSE"}
for key in student:
    print(key)
# OUTPUT:
# name
# age
# branch


# PRINT VALUES USING LOOP:

student = {"name":"Shivam","age":18,"branch":"CSE"}
for value in student.values():
    print(value)
# OUTPUT:
# Shivam
# 18
# CSE


# PRINT KEY AND VALUE USING LOOP:
# items() ka use karke key aur value dono ko ek saath access kar sakte hain.

student = {"name":"Shivam","age":18,"branch":"CSE"}
for key,value in student.items():
    print(key,value)
# OUTPUT:
# name Shivam
# age 18
# branch CSE