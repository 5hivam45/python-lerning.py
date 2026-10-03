# CHAPTER 7 — LOOPS IN PYTHON
# PRACTICE SET

# QUESTION 1: MULTIPLICATION TABLE USING FOR LOOP

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# INPUT:
# Enter a number: 5
# OUTPUT:
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50


# QUESTION 2: GREET NAMES STARTING WITH S

names = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in names:
  if name.startswith("S"):
    print("Hello", name)

# OUTPUT:
# Hello Sohan
# Hello Sachin


# QUESTION 3: MULTIPLICATION TABLE USING WHILE LOOP

n = int(input("Enter a number: "))
i = 1
while i <= 10:
  print(n * i)
i += 1

# INPUT:
# Enter a number: 6
# OUTPUT:
# 6
# 12
# 18
# 24
# 30
# 36
# 42
# 48
# 54
# 60


