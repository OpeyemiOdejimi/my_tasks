# A  to do list

"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""



# # Take in tasks

# tasks = []

# # Add task

# def add_task(task):
#     tasks.append(task)
#     print(f" Add this {task}")



# # Function to remove a task from the list
# def remove_task(task):
#     if task in tasks:
#         tasks.remove(task)
#         print(f'Task "{task}" removed!')



# # Loops to collect task options

# while True:
#     print("\nOptions: \n1. Add Task \n2. Remove task \n3. Exit")
#     print(" ")


#     user_option = input("Pick an option: ")

#     if user_option == "1":
#         task = input(" Add Task: ")
#         add_task(task)

#     elif user_option == "2":
#         task = input("Remove task: ")
#         remove_task(task)
    
#     elif user_option == "3":
#         print("Just exit the program.!")
#         break
#     else:
#         print('You haven\'t picked a valid option')
















"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""


# @title continue...

# Function to slice the email into username and domain
def email_slicer(email):
    # Check if the email contains "@" and "." in the domain part
    if "@" in email and '.' in email.split('@')[1]:
        # Split the email into username and domain
        username, domain = email.split('@')
        return username, domain
    else:
        # Return None if the email format is invalid
        return None, None

# Get email input from the user
email = input("Enter your email address: ")

# Call the function to slice the email
username, domain = email_slicer(email)

# Display the result
if username and domain:
    print(f"Username: {username}\nDomain: {domain}")
else:
    print("Invalid email format! Please enter a valid email.")