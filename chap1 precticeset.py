# PROBLEM 1:
# we can use triple quotes to write a multiple lines in python

# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.
# ''')

# PROBLEM 2:

# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("MY NAME IS SHIVAM KUMAR SINGH AND I AM LERNING PYTHON PROGRAMING LANGUAGE")
# engine.runAndWait()


# PROBLEM 3:

import os

# Specify the directory path ('.' refers to the current working directory)
directory_path = "/"  # Replace with the actual path you want to check

try:
    # os.listdir() returns a list of all files and folders in the path
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(f"- {item}")

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")