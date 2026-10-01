# PROBLEM:1

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1:",a1)
    
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2:",a2)
    
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3:",a3)
    
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4:",a4)
    
# OUTPUT WILL BE =
# Enter number 1: 1
#    Enter number 2: 2
#    Enter number 3: 3
#    Enter number 4: 4
#    Greatest number is a4: 4


# PEOBLEM:2

# marks1 = int(input("Enter number 1: "))
# marks2 = int(input("Enter number 2: "))
# marks3 = int(input("Enter number 3: "))

# # check for total percentage
# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you are passed:",total_percentage)
    
# else:
#     print("you are failed,try again next year:",total_percentage)
    
# OUTPUT WILL BE =
# Enter number 1: 70
# Enter number 2: 50
# Enter number 3: 45
# you are passed: 55.0


# PROBLEM:3

# message = input("Enter your message: ")

# if ("make money" in message.lower() or
#     "buy now" in message.lower() or
#     "subscribe" in message.lower() or
#     "click here" in message.lower()):
#     print("This message is spam")
# else:
#     print("This message is not spam")
# OUTPUT WILL BE = 
# Enter your message: you buy now
# This message is spam


# PROBLEM:4

# username = input("Enter username: ")

# if len(username) < 10:
#     print("Username contains less than 10 characters")
# else:
#     print("Username contains 10 or more characters")
    
# OUTPUT WILL BE = 
# Enter username: shivam
# Username contains less than 10 characters

# PROBLEM:5

# names = ["Shivam", "Aman", "Rahul", "Rohit"]

# name = input("Enter name: ")

# if name in names:
#     print("Name is present in the list")
# else:
#     print("Name is not present in the list")
    
# OUTPUT WILL BE = 
# Enter name: shivam
# Name is not present in the list


# PROBLEM:6

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")
    
# OUTPUT WILL BE = 
# Enter your marks: 66.7
# Grade: D