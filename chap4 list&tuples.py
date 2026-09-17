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
# number.extend([6])
# print(number) #OUTPUT=[1, 2, 3, 4, 5, 6]

# remove:
# numbers = [10,20,30]
# numbers.remove(20)
# print(numbers) # OUTPUT=[10, 30, 40]

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
