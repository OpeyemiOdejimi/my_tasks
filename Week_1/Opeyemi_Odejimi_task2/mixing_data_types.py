# Mixing Data Types
# - Ask the user for:
#    * Your age(integer)
#    * Your height in meters(float)
#    * Your name(string)
#  - Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.

age = input("Enter your age:")
height = float(input("Enter your height in meters:"))
name = input("Enter your name:")

print(f"My is {name}, I am {age} years old and currently my height is {height} meters.")