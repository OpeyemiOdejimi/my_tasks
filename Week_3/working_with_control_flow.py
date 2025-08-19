# Control Flow in Python
# * Control flow refers to the order in which statements are executed in a program. Instead of always running line by line, control flow allows your program to: 
# * Make decisions (choose one path or another, explore alternatives).
# * Exit or skip parts of code
# It is the foundation for logic and problem solving in programming. 
# COntrol flow is divided into 3 parts


# A. Conditional Statements
#  1. if Statement
#  * Executes a block only when a condition is true.

age = 20
if age >= 18:
    print("You are eligble to vote") # Output: You are eligible to vote

# Some usecases
# * Checking for eligibility.
# * Validating login attempts.
# * Ensuring a minimum purchase requirments, etc.

# 2. if-else Statement
# Provides two alternative paths

wallet = 400
price = 500

if wallet >= price:
    print("Purchase succesful")
else:
    print("Insufficient balance") # Insufficient balance


# Some usecases
# * Deciding success or failure of a payment
# * Granting or denying access to a system.
# * Determining pass/fail in an exam, etc.

# 3. if-elif-else Statement
# * Used for multiple conditions

score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

# Some usecases
# * Student grading systmes.
# * Assigning ticket categories (VIP, Regular, Student).
# Categorizing temperatures (Hot, Warm, Cold), etc.

# 4. Nested if
# * Placing an if inside another if

age = 16
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

# Some usecases
# *Voting eligibility (age + citizenship)
# * Banking (accounnt active + balance sufficient)
# * School admission (age + grade level)


# B. Loops
# 1. for loop
#  * This is used for iterating over a sequence (strings, list, tuple, dictionary)

# Iterates through each element in a LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")


## Some usecases
# Iterating through shopping lists.
# Checking availability of products.

# Displaying student names, etc.


# Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

# Output: 
# Point: 0.34654
# Point: -0.48585
# Point: 0.57477


# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")


## Some usecases