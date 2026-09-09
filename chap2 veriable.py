# VARIABLE AND DATATYPES

# a=1  #VARIABLES = CONTAINER TO STORE A VALUE.
# b="SHIVAM"  #KEYWORDS = RESERVED WORDS IN PYTHON THAT HAVE A SPECIAL MEANING AND CANNOT BE USED AS VARIABLE NAMES.
# NAME="SHIVAM"  #IDENTIFIERS = NAMES GIVEN TO VARIABLES, FUNCTIONS, CLASSES, OR OTHER OBJECTS IN PYTHON.


# DATATYPES:
# 1. Numeric Types: int, float, complex
# 2. Text Type: str
# 3. Boolean Type: bool
# 4. Sequence Types: list, tuple, range
# 5. Mapping Type: dict
# 6. Set Types: set, frozenset
# 7. Binary Types: bytes, bytearray, memoryview

# EXAMPLES:
# a=10  #int A IS AN INTEGER DATA TYPE
# b=3.14  #float B IS A FLOAT DATA TYPE
# c=1+2j  #complex C IS A COMPLEX DATA TYPE
# d="Hello, World!"  #str D IS A STRING DATA TYPE
# e=True  #bool E IS A BOOLEAN DATA TYPE
# f=[1, 2, 3, 4, 5]  #list F IS A LIST DATA TYPE
# g=(1, 2, 3, 4, 5)  #tuple G IS A TUPLE DATA TYPE
# h=range(5)  #range H IS A RANGE DATA TYPE
# i={"name": "Shivam", "age": 25}  #dict I IS A DICTIONARY DATA TYPE
# j={1, 2, 3, 4, 5}  #set J IS A SET DATA TYPE
# k=frozenset([1, 2, 3, 4, 5])  #frozenset K IS A FROZENSET DATA TYPE
# l=b"Hello"  #bytes L IS A BYTES DATA TYPE
# m=bytearray(b"Hello")  #bytearray M IS A BYTEARRAY DATA TYPE
# n=memoryview(b"Hello")  #memoryview N IS A MEMORYVIEW DATA TYPE
# O= None  #None O IS A NONE DATA TYPE


# RULES FOR NAMING VARIABLES:
# 1. Variable names can contain letters, numbers, and underscores (_).
# 2. Variable names cannot start with a number.
# 3. Variable names are case-sensitive.
# 4. Variable names cannot be the same as reserved keywords in Python.

# EXAMPLES OF VALID VARIABLE NAMES:
# a=23 #valid variable name (can start with a letter)
# aaa=432 #valid variable name (can contain letters)
# _a=567 #valid variable name (can start with underscore)
# A=890 #valid variable name (can be uppercase)
# shivam_kumar=1234 #valid variable name (can contain underscore)
# _shivam=5678 #valid variable name (can start with underscore)
# @shivam=9012  #INVALID VARIABLE NAME (CANNOT START WITH @)
# shivam-kumar=3456  #INVALID VARIABLE NAME (CANNOT CONTAIN -)
# 123shivam=7890  #INVALID VARIABLE NAME (CANNOT START WITH A NUMBER)


# TYPEA() FUNCTION AND TYPECASTING:
# The type() function is used to determine the data type of a variable or value in Python
# Example:
a = 5
print(type(a))  # Output will be <class 'int'>