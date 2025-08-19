# # Python Operators
# # * Operators are special symbols in Python that perform operations on variables and values. Here we will focus on;
# # * Comparison Operators
# # * Assignment Operators
# # * Logical Operators

# # Comparison Operators
# # * Comparison operators are used to compare two values.
# # * Comparison operators are used to compare twoo values. The result is always True or False

# a = 10
# b = 20

# print(a == b)  #False
# print(a != b)  # True
# print(a > b)  # False
# print(a < b)  # True
# print(a >= 10) # True
# print( a <= 25) # True

# # Use case Example- Student Exam Result

# score = 75

# print(score >= 50)  # True (Passed)
# print(score < 50)   # False (Failed)
# print(score == 100) # False (Not full marks)


# # Assignment Operators
# # * Assignment Operators
# # * Assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing x = x + 5, we can write x += 5.


# x = 10
# print("Initial value:", x)

# x += 5
# print("After x +=5:", x)

# x -= 2
# print("After x -= 2:", x)

# x *= 3
# print("after x *= 3:", x)

# x %= 3
# print("After x %= 3:", x)

# x = 4
# x **= 2
# print("After x **=2:", x)

# x //= 3
# print("After x //= 3:", x)

# # Use case Exammple:

# # Define variables
# balance = 1000
# deposit = 200
# withdraw = 150

# balance += deposit # Add deposit
# balance -= withdraw # Subtract withdrawal

# print("Updated Balance:", balance)
# # Output: Updated Balance: 1050

# # Logical Operators

# # * Logical operators are used to combine conditional statements. They work with Boolean values (True or False).

# x = 10
# y = 20

# # and operator
# print(x > 5 and y > 15)  # True

# # or operator
# print(x < 5 or y > 15)   # True

# # not operator
# print(not(x == 10))      # False


# # Use case example1 - Scholarship Eligibility

# # Define variables

# age = 17
# score = 85

# # Must be younger than 18 AND score above 80
# eligible = (age < 18) and (score > 80)

# print("Scholarship Eligible:", eligible)
# # Output: Scholarship Eligible: True

# # Use case example2 - Event Access

# age = 22
# has_ticket = False

# can_enter = (age >= 18) and (has_ticket or age < 25)

# print("Access Granted:", can_enter)
# # Output: Access Granted: True (because age < 25 even without ticket)



print("*** UNILAG Admission Eligibility Checker (2025/2026) ***")

# Collecting user name
name = input("Enter your name: ")

# Age requirement 
age = int(input("Enter your age: "))

# UTME requirement 
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Did you choose UNILAG as your first choice? (Yes/No): ").title()

# O'Level requirement 
olevel_credits = int(input("How many credit passes did you have in one sitting? "))
english_pass = input("Did you pass English Language? (Yes/No): ").title()
math_pass = input("Did you pass Mathematics? (Yes/No): ").title()

# Post-UTME screening 
post_utme_score = int(input("Enter your Post-UTME score (0-100): "))

# Step 5: Departmental cut-off (asking user)
dept_cutoff = int(input("Enter your Departmental cut-off mark (200 - 320): "))

# Conditions for considering the user admission
# must be at least 16
meets_age = age >= 16
# must be >= 200 and UNILAG as first choice
meets_utme = (utme_score >= 200) and (first_choice == "Yes")
# must be 5 credits including English & Math
meets_olevel = (olevel_credits >= 5) and (english_pass == "Yes") and (math_pass == "Yes")

# total score for admission = UTME + Post-UTME
total_score = utme_score + post_utme_score

meets_cutoff = total_score >= dept_cutoff

# Final decision
eligibility = meets_age and meets_utme and meets_olevel and meets_cutoff
# mapping true and false to statement for final result
result = {
    True: f"Congratulations {name}, you have been offered admission to the course of your choice", 
    False: f"Sorry, no admission yet" 
}

print("\n=== Admission Status ===")
print(f"Status: {result[eligibility]}")