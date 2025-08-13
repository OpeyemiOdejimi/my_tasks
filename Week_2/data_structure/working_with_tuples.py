# Tuples
# * A tuple is an ordered, immutable (unchangeable) collection of items in Python.
# Creating Tuples
# 1. Using parenthesis()

# Example 1: tuple with multiple items
fruits = ("apple", "banana","cherry")
print(fruits)  # ('apple', 'banana')

# 2. Without parentheses (tuple packing)

numbers = 1, 2, 3
print(numbers) # (1,2,3)

# 3. Single-item tuple (must include a comma)

single_item = ("apple",)
print(single_item)  # ('apple')
print(type(single_item)) # <class 'tuple'>

# 4. Using the tuple() constructor

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) # ('apple', 'banana', 'cherry')


# Characteristics of Tuples

# 1. Ordered - Items have a fixed position
# 2. Immutable - Cannot change after creation
# 3. Allow duplicates - Same value can appear multiples times
# 4. Can contain mixed data types - Strings, integers, lists, etc
# 5. Can be nested - Tuples inside tuples

# Ordered
colors = ("red", "green", "blue")
print(colors[0])# red

# Immutable (uncomment and run. This will cause an error)
#colors[1] = "yellow" # TypeError

# Allows duplicates
numbers = (1, 2, 2, 3)
print(numbers) #(1,2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed) # ('apple', 3, True, 5.6)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) #(('a', 'b'), (1, 2))

# Tuple Operations
# * Even though tuples are immutable, you can stil perform several operations

# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1]) # banana
print(fruits[-1]) # cherry

# 2. Slicing 
print(fruits[0:2])  # ('apple', 'banana')
print(fruits[::-1]) # ('Cherry', 'banana', 'apple')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) # (1, 2, 3, 4)

# 4. Repitition
nums = (1, 2)
print(nums * 3) # (1, 2, 1, 2, 1, 2)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits) # True
print("grape" not in fruits) # True

# 6. Iteration
for fruits in fruits:
    print(fruits)



# Working with Tuples
# You can't modify a tuple directly, but you can
#   * Convert it to a list, modify it, then convert back.
#   * Use built-in functions to work with tuple contents


# 1. Unpacking Tuples


person = ("John", 25, "Nigeria", 1.2)
name, age, country, prompt = person
print(name) # John
print(age) # 25
print(country) # Nigeria
print(prompt)
# 1. Tuples Methods

#   * Tules have only two methods
# don't count() and dot index()

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2)) # 2 (counts occurences of 2)
print(numbers.index(3)) # 3 (position of first occurrence of 3)

# Converting Between List and Tuple

# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# List back to Tuple
t = tuple(lst)
print(t) # (1, 2, 3, 4)

# Built in Functions with Tuples

nums = (4, 1, 7, 3)

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))