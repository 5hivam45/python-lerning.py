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


# QUESTION 4: CHECK PRIME NUMBER

n = int(input("Enter a number: "))

is_prime = True

if n <= 1:
    is_prime = False

else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")

else:
    print("Not a prime number")

# INPUT:
# Enter a number: 7
# OUTPUT:
# Prime number
# ANOTHER EXAMPLE:
# INPUT: 8
# OUTPUT: Not a prime number


# QUESTION 5: SUM OF FIRST N NATURAL NUMBERS

n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
 total += i
i += 1

print("Sum =", total)

# INPUT:
# Enter n: 5
# OUTPUT:
# Sum = 15
# CALCULATION:
# 1 + 2 + 3 + 4 + 5 = 15


# QUESTION 6: FACTORIAL USING FOR LOOP

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
 factorial *= i

print("Factorial =", factorial)

# INPUT:
# Enter a number: 5
# OUTPUT:
# Factorial = 120
# CALCULATION:
# 5 * 4 * 3 * 2 * 1 = 120


