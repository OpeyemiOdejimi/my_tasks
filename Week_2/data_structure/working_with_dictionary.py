# Python Dictionaries
# * A dictionary in Python is a collection of key-value pairs
#   * Keys are unique and used to store and retrieve values
#   * Values can be any data type (string, integer, list, tuple, even another dictionary).

# Syntax
# dictionary_name = {key1: value1, key2: value2}

# Characteristics of Dictionaries

# 1. Key-Value Structure: Each item is stored as a key: value pair.
# 2. Mutable: You can add, change, or remove items.
# 3. Unordered (before Python 3.7): From Python 3.7+, they maintain insertion order.
# 4. Unnique Keys: No duplicate keys allowed; a new assignment to an existing key overwrites the old value.
# 5. Keys must be immutable: Strings, numbers, tuples (containing only immutable items) can be keys.

# Creating Dictionaaries

# 1. Using curly braces

student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# 2. Using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)

# 3. Empty dictionary
empty_dict = {}
print(empty_dict)


#. Dictionary Comprehension

# Syntax: 
# {key_expression: value_expression for item in iterable if condition}

# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# with Condition

# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)


# From Existing Dictionary

students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)

passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)

# Using Strings Keys

names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Accessing Dictionary Items

# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Using Key
print(student["name"])

# Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "Not Found"))

# Modifying Dictionaries

student["age"] = 21  #Change value 
student ["grade"] = "A"  #Add new key-value pair
print(student)

# Removing Items from Dictionaries

# 1. Using pop()
student.pop("grade")

# 2. Using popitem() - removes last inserted key-value
student.popitem()
print(student)

# 3. Using del keyword
# del student ["course"]

# 4. using clear() - removes all items
student.clear()

print(student)

# Dictionary Methods