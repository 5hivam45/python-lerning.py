# LIST:python list are containers to store a set of value of any data type 

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
# | Method      | Kaam                                 | Example           |
# | ----------- | ------------------------------------ | ----------------- |
# | `append()`  | End me item add karta hai            | `a.append(5)`     |
# | `insert()`  | Specific position par item add       | `a.insert(1, 5)`  |
# | `extend()`  | Multiple items add                   | `a.extend([4,5])` |
# | `remove()`  | Item ko remove karta hai             | `a.remove(5)`     |
# | `pop()`     | Item ko position se remove karta hai | `a.pop(1)`        |
# | `clear()`   | Puri list empty karta hai            | `a.clear()`       |
# | `sort()`    | List ko sort karta hai               | `a.sort()`        |
# | `reverse()` | List ko ulta karta hai               | `a.reverse()`     |
# | `index()`   | Item ki position batata hai          | `a.index(5)`      |
# | `count()`   | Item kitni baar hai                  | `a.count(5)`      |
# | `copy()`    | List ki copy banata hai              | `b = a.copy()`    |

# append:
# name = ["apple","orange",5,345.06,False,"Aakash","shivam"]
# name.append("ishan")
# print(name) #OUTPUT=['apple', 'orange', 5, 345.06, False, 'Aakash', 'shivam', 'ishan']

# # 2
# numbers = [10, 20, 30]

# numbers.append(40)
# print(numbers) #OUTPUT= [10, 20, 30, 40]

# insert:
# number = [1,2,3,4,5]
# number.insert(2,6)
# print(number) #OUTPUT=[1, 2, 6, 3, 4, 5]

# extend:
# number = [1,2,3,4,5]
# number.extend([6,7,8])
# print(number) #OUTPUT=[1, 2, 3, 4, 5, 6,7,8,]

# remove:
# numbers = [10,20,30]
# numbers.remove(20)
# print(numbers) # OUTPUT=[10, 30]

# pop:
# number = [1,2,3,4,5]
# number.pop(1)
# print(number) #OUTPUT= [1, 3, 4, 5]

# clear:
# number = [1,2,3,4,5]
# number.clear()
# print(number) #OUTPUT=[]

# sort:
# number = [1.2,4.5,3.3,2.2]
# number.sort()
# print(number) #OUTPUT=[1.2, 2.2, 3.3, 4.5]

# reverse:
# numbers = [10,20,30,40,50]
# numbers.reverse()
# print(numbers)

# index:
# number = [1,2,3,4,5]
# print(number.index(3)) #OUTPUT=2

# count:
# number = [1,2,1,3,1]
# print(number.count(1)) #OUTPUT=3

# copy:
# number = [1,2,3,4,5]
# new_number = number.copy()
# print(number)
# print(new_number) #OUTPUT=[1, 2, 3, 4, 5]
#                           [1, 2, 3, 4, 5]

# TUPLE:pyton tuple are container to store a set of value of any data type 

# 1:
# name  =("apple","orange",5,345.06,False,"Aakash","shivam")
# print(name[2]) #OUTPUT=5

# 2:
# name = ("apple","orange",5,345.06,false,"Aakash","shivam")
# name[2]=8
# print(name[2]) #OUTPUT=ERROR
# unlike lists tuple are immutable (we cannot change the value of tuple)

# 3:
# name = ("apple","orange",5,345.06,False,"Aakash","shivam")
# print(name[1:3]) #OUTPUT=('orange', 5)

# TUPLE PROPERTIES:
# 1.tuple is ordered
# 2.tuple is immutable
# 3.tuple allows duplicate value 
# 4.tuple can store different data types
# 5.tuple uses () brackets

# TUPLE METHODS:
# |------|-------------------|------|
# | count() | Item kitni baar hai | a.count(5) |
# | index() | Item ki position batata hai | a.index(5) |

# count():
# number = (1,2,1,3,1)
# print(number.count(1)) #OUTPUT=3
# count() batata hai ki koi item tuple me kitni baar present hai

# 2:
# fruits = ("apple","banana","apple","mango","apple")
# print(fruits.count("apple")) #OUTPUT=3

# index():
# number = (1,2,3,4,5)
# print(number.index(3)) #OUTPUT=2
# index() item ki first position/index batata hai

# 2:
# number = (10,20,30,20,40)
# print(number.index(20)) #OUTPUT=1
# agar item multiple times present hai to index() first occurrence ka index deta hai

# len():
# number = (10,20,30,40,50)
# print(len(number)) #OUTPUT=5
# len() tuple ke andar total items ki number batata hai

# IN:
# fruits = ("apple","orange","mango")
# print("apple" in fruits) #OUTPUT=True
# print("banana" in fruits) #OUTPUT=False
# "in" check karta hai ki item tuple ke andar present hai ya nahi

# NOT IN:
# fruits = ("apple","orange","mango")
# print("banana" not in fruits) #OUTPUT=True
# print("apple" not in fruits) #OUTPUT=False

# TUPLE INDEXING:

# number = (10,20,30,40,50)
# print(number[0]) #OUTPUT=10
# print(number[2]) #OUTPUT=30
# print(number[-1]) #OUTPUT=50

# TUPLE SLICING:

# number = (10,20,30,40,50)
# print(number[1:4]) #OUTPUT=(20, 30, 40)
# print(number[:3]) #OUTPUT=(10, 20, 30)
# print(number[2:]) #OUTPUT=(30, 40, 50)
# print(number[::-1]) #OUTPUT=(50, 40, 30, 20, 10)

# SINGLE ITEM TUPLE:

# x = (10)
# print(type(x)) #OUTPUT=<class 'int'>
# x = (10,)
# print(type(x)) #OUTPUT=<class 'tuple'>
# single item tuple banane ke liye comma (,) zaroori hai

# TUPLE CONCATENATION:

# a = (1,2,3)
# b = (4,5,6)
# c = a + b
# print(c) #OUTPUT=(1, 2, 3, 4, 5, 6)
# + operator se do tuples ko join kar sakte hain

# TUPLE REPETITION:

# a = (1,2,3)
# print(a * 3) #OUTPUT=(1, 2, 3, 1, 2, 3, 1, 2, 3)
# * operator se tuple ko multiple times repeat kar sakte hain