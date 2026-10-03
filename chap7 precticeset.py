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


