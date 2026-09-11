# OPERATORS IN PYTHON

# 1. ARITHMETIC OPERATORS:
#    + (Addition)
#    - (Subtraction)
#    * (Multiplication)
#    / (Division)
#    % (Modulus)
#    ** (Exponentiation)
#    // (Floor Division)

# ASSIGNMENT OPERATORS:
#    = (Assign)
#   += (Add and assign)
#   -= (Subtract and assign)
#   *= (Multiply and assign)
#   /= (Divide and assign)
#   %= (Modulus and assign)
#   **= (Exponentiation and assign)
#   //= (Floor Division and assign)

# 2. COMPARISON OPERATORS:
#    == (Equal to)
#    != (Not equal to)
#    < (Less than)
#    > (Greater than)
#    <= (Less than or equal to)
#    >= (Greater than or equal to)

# 3. LOGICAL OPERATORS:
#    and (Returns True if both statements are true)
#    or (Returns True if one of the statements is true)
#    not (Reverses the result, returns False if the result is true)

# 4. IDENTITY OPERATORS:
#    is (Returns True if both variables are the same object)
#    is not (Returns True if both variables are not the same object)

# 5. MEMBERSHIP OPERATORS:
#    in (Returns True if a sequence with the specified value is present in the object)
#    not in (Returns True if a sequence with the specified value is not present in the object)

# EXAMPLE 
# ARITHMETIC OPERATORS:
# a = 10
# b = 5
# c = a + b  # Addition output will be 15
# d = a - b  # Subtraction output will be 5
# e = a * b  # Multiplication output will be 50
# f = a / b  # Division output will be 2.0
# g = a % b  # Modulus output will be 0
# h = a ** b # Exponentiation output will be 100000
# i = a // b # Floor Division output will be 2
# print(c)

# ASSIGNMENT OPERATORS:
# a += b  # a = a + b, output will be 15
# a -= b  # a = a - b, output will be 5
# a *= b  # a = a * b, output will be 50
# a /= b  # a = a / b, output will be 2.0
# a %= b  # a = a % b, output will be 0
# a **= b # a = a ** b, output will be 100000
# a //= b # a = a // b, output will be 2

# COMPARISON OPERATORS:
# a == b  # Returns False
# a != b  # Returns True
# a < b   # Returns False
# a > b   # Returns True
# a <= b  # Returns False
# a >= b  # Returns True 

# EXAMPLE
# a=5==5
# print(a)  # Output will be True

# a=5!=5
# print(a)  # Output will be False

# a=5>5
# print(a)  # Output will be False

# a=5<5
# print(a)  # Output will be False

# a=5>=5
# print(a)  # Output will be True

# a=5<=5
# print(a)  # Output will be True  

# LOGICAL OPERATORS:
# a = True and False  # Returns False
# a = True or False   # Returns True
# a = not True        # Returns False

# TRUTH TABLES FOR LOGICAL OPERATORS:
# AND OPERATOR:
# True and True   # Returns True
# True and False  # Returns False
# False and True  # Returns False
# False and False # Returns False

# OR OPERATOR:
# True OR True    # Returns True
# True OR False   # Returns True
# False OR True   # Returns True
# False OR False  # Returns False

# NOT OPERATOR:
# not True   # Returns False
# not False  # Returns True



# type() FUNCTION AND TYPECASTING:
# type() function is used to determine the data type of a variable or value in Python
# typecasting is the process of converting one data type to another

# Example of type() function:
# a = 5
# print(type(a))  # Output will be <class 'int'>

# b = 5.0
# print(type(b))  # Output will be <class 'float'>

# c = "Hello"
# print(type(c))  # Output will be <class 'str'>

# # Example of typecasting:
# d = float(a)  # Converting integer to float
# print(type(d))  # Output will be <class 'float'>
# print(d)        # Output will be 5.0

# e = int(b)    # Converting float to integer
# print(type(e))  # Output will be <class 'int'>
# # print(e)        # Output will be 5



# input() FUNCTION:
# The input() function is used to take input from the user
# name = input("Enter your name: ")
# print("Hello, " + name)

# example of input() function:
# age = input("Enter your age: ")
# print("You are " + age + " years old.")

# example 2:
# weight = input("Enter your weight: ")
# print("Your weight is " + weight + " kg.")

# example 3:
# height = input("Enter your height: ")
# print("Your height is " + height + " cm.")


