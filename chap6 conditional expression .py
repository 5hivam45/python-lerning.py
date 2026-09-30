# CONDITIONAL EXPRESSION:

# Conditional Expression Python me if-else ko short aur one-line me likhne ka tarika hai.
# Isse Ternary Operator bhi kaha jata hai.

age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)
# OUTPUT=Adult


# SYNTAX:
# value_if_true if condition else value_if_false

# Condition True hone par first value return hogi aur False hone par second value return hogi.


# 1: CONDITIONAL EXPRESSION WITH IF-ELSE:

# Normal if-else:

age = 18
if age >= 18:
    result = "Adult"
else:
    result = "Minor"
print(result)
# OUTPUT=Adult

Conditional Expression:

age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)
# OUTPUT=Adult


# 2: CONDITIONAL EXPRESSION IN PRINT():
# Conditional Expression ko directly print() ke andar bhi use kar sakte hain.

age = 15
print("Adult" if age >= 18 else "Minor")
# OUTPUT=Minor


# 3: CONDITIONAL EXPRESSION WITH NUMBERS:
# Conditional Expression se numbers bhi return kar sakte hain.

a = 10
b = 20
greater = a if a > b else b
print(greater)
# OUTPUT=20


