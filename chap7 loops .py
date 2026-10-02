# LOOPS IN PYTHON:

# Loop: Python me loop ka use kisi code ko baar-baar execute karne ke liye hota hai.
# Python me humne mainly while loop aur for loop padha hai.


# 1: WHILE LOOP:
# while loop tab tak code ko repeat karta hai jab tak condition True hoti hai.

i = 1
while i <= 5:
    print(i)
    i += 1

# OUTPUT=
# 1
# 2
# 3
# 4
# 5
# Condition False hote hi loop stop ho jata hai.


# 2: BREAK:
# break ka use poore loop ko turant stop karne ke liye hota hai.

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# OUTPUT=
# 1
# 2
# break lagte hi loop completely stop ho jata hai.


# 3: CONTINUE:
# continue ka use current iteration ko skip karne ke liye hota hai.

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# OUTPUT=
# 1
# 2
# 4
# 5
# continue loop ko stop nahi karta, sirf current iteration skip karta hai.


# 4: FOR LOOP:
# for loop ka use kisi sequence ke elements ko one by one access karne ke liye hota hai.

numbers = [10,20,30,40,50]

for i in numbers:
    print(i)

# OUTPUT=
# 10
# 20
# 30
# 40
# 50
# for loop sequence ke har element par one by one run hota hai.


# 5: RANGE():
# range() numbers ki ek sequence generate karta hai.
# range(stop):
# range(stop) me counting 0 se start hoti hai aur stop se pehle tak chalti hai.

for i in range(5):
    print(i)

# OUTPUT=
# 0
# 1
# 2
# 3
# 4
# IMPORTANT: stop value include nahi hoti.


# range(start, stop):
# Isme counting start se start hoti hai aur stop se pehle tak chalti hai.

for i in range(2,6):
    print(i)

# OUTPUT=
# 2
# 3
# 4
# 5


# range(start, stop, step):
# step batata hai ki har iteration me value kitni increase ya decrease hogi.

for i in range(2,10,2):
    print(i)

# OUTPUT=
# 2
# 4
# 6
# 8


# Negative Step:
# Negative step se counting reverse direction me hoti hai.

for i in range(10,2,-2):
    print(i)

# OUTPUT=
# 10
# 8
# 6
# 4


# RANGE() RULE:
# range	Values
# range(5)	0,1,2,3,4
# range(2,6)	2,3,4,5
# range(2,10,2)	2,4,6,8
# range(10,2,-2)	10,8,6,4

# IMPORTANT:

# Start value include hoti hai.
# Stop value include nahi hoti.
# range(n) me counting 0 se start hoti hai.
# Har range 0 se start nahi hoti.


# 6: FOR LOOP + CALCULATION:
# Loop ke andar current i value par calculation hoti hai.

for i in range(1,5):
    print(i + 1)

# OUTPUT=
# 2
# 3
# 4
# 5
for i in range(1,5):
    print(i * 2)

# OUTPUT=
# 2
# 4
# 6
# 8
# i + 1, i * 2 etc. har iteration me current i ke according calculate hote hain.


# 7: FOR LOOP + IF:
# for loop ke andar if condition ka use karke specific values ko check kar sakte hain.

for i in range(1,8):
    if i % 2 == 0:
        print(i)

# OUTPUT=
# 2
# 4
# 6
# Yaha i % 2 == 0 ka matlab number even hai.

for i in range(1,8):
    if i % 2 != 0:
        print(i)

# OUTPUT=
# 1
# 3
# 5
# 7
# Yaha i % 2 != 0 ka matlab number odd hai.


# 8: BREAK IN FOR LOOP:
# for loop me bhi break poore loop ko stop kar deta hai.

for i in range(1,8):
    if i == 5:
        break
    print(i)

# OUTPUT=
# 1
# 2
# 3
# 4
# IMPORTANT: Sirf if condition loop ko stop nahi karti. Loop stop karne ke liye break chahiye.


# 9: CONTINUE IN FOR LOOP:
# continue current iteration ko skip karta hai aur loop next iteration par chala jata hai.

for i in range(1,6):
    if i == 3:
        continue
    print(i)

# OUTPUT=
# 1
# 2
# 4
# 5
# Yaha 3 skip ho gaya.


# 10: NESTED LOOPS:
# Ek loop ke andar doosra loop ho to use nested loop kehte hain.

for i in range(2):
    for j in range(3):
        print(i,j)

# OUTPUT=
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2

# Rule:
# Outer loop ki ek value fix hoti hai aur inner loop apni poori range complete karta hai.
# Phir outer loop ki next value aati hai.


# 11: NESTED LOOP + CALCULATION:
# Nested loop me i aur j dono ki values ke saath calculation kar sakte hain.

for i in range(2):
    for j in range(3):
        print(i + j)

# OUTPUT=
# 0
# 1
# 2
# 1
# 2
# 3
for i in range(2):
    for j in range(3):
        print(i * j)

# OUTPUT=
# 0
# 0
# 0
# 0
# 1
# 2
for i in range(2):
    for j in range(3):
        print(i * j + 1)

# OUTPUT=
# 1
# 1
# 1
# 1
# 2
# 3

# 12: PATTERN PRINTING:
# Nested loops ka use patterns print karne ke liye bhi kiya ja sakta hai.
# print("*", end=" ") same line me star print karta hai.
# print() next line me le jata hai.

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# OUTPUT=
# * * *
# * * *
# * * *

# IMPORTANT:
# Outer loop = rows
# Inner loop = har row me items/stars


# 13: INCREASING PATTERN:
for i in range(4):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# OUTPUT=
# *
# * *
# * * *
# * * * *
# Yaha har new row me stars ki quantity 1 se increase hoti hai.


# 14: DECREASING PATTERN:
for i in range(4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# OUTPUT=
# * * * *
# * * *
# * *
# *
# Yaha har new row me stars ki quantity decrease hoti hai.


# 15: FOR LOOP + IF/ELSE:
# if/else ka use loop ke andar condition ke according different output dene ke liye kar sakte hain.

for i in range(1,6):
    if i == 3:
        print("three")
    else:
        print(i)

# OUTPUT=
# 1
# 2
# three
# 4
# 5
# IMPORTANT: if condition True hone par sirf us iteration ka code change hota hai. Loop automatically stop nahi hota.


