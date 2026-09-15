# LIST:python lit are containers to store a set of value of any data type 

# 1:
# name = ["apple","orange",5,345.06,False,"Aakash","shivam"]
# print(name[2]) #OUTPUT=5

# # 2:
# name = ["apple","orange",5,345.06,False,"Aakash","shivam"]
# name[2]=8
# print(name[2]) #unlike stings lists are mutable 
# print(name) #OUTPUT=['apple', 'orange', 8, 345.06, False, 'Aakash', 'shivam']

# 3:
# name = ["apple","orange",5,345.06,False,"Aakash","shivam"]
# print(name[1:3]) #OUTPU=['ORANGE',5]


# LIST METHODS:
# append.
name = ["apple","orange",5,345.06,False,"Aakash","shivam"]
name.append("ishan")
print(name) #OUTPUT=['apple', 'orange', 5, 345.06, False, 'Aakash', 'shivam', 'ishan']

# 2
numbers = [10, 20, 30]

numbers.append(40)
print(numbers) #OUTPUT= [10, 20, 30, 40]


# remove.
numbers = [10,20,30]
numbers.remove(20)
print(numbers) # OUTPUT=[10, 30, 40]
