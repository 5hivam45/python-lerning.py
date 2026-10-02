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


