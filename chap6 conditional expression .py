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


# 4: EVEN OR ODD:
# Number even hai ya odd, ye check karne ke liye % operator use karte hain.
# Agar number ko 2 se divide karne par remainder 0 aaye to number Even hota hai.
# Agar remainder 0 na aaye to number Odd hota hai.

number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)
# OUTPUT=Odd

number = 8
result = "Even" if number % 2 == 0 else "Odd"
print(result)
# OUTPUT=Even


# 5: CONDITIONAL EXPRESSION WITH COMPARISON:
# Different comparison operators ke saath bhi Conditional Expression use kar sakte hain.

a = 10
b = 20
result = "a is greater" if a > b else "b is greater"
print(result)
# OUTPUT=b is greater


# 6: CONDITIONAL EXPRESSION WITH BOOLEAN:
# Conditional Expression True aur False ke saath bhi use kar sakte hain.

age = 20
result = True if age >= 18 else False
print(result)
# OUTPUT=True


# 7: CONDITIONAL EXPRESSION WITH LOGICAL OPERATORS:
# and, or, not jaise logical operators bhi condition me use kar sakte hain.

age = 20
has_id = True
result = "Allowed" if age >= 18 and has_id else "Not Allowed"
print(result)
# OUTPUT=Allowed


