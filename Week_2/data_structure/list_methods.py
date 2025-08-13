9### List Methods

# Python provides many bult-in methods working with lists. Here is each method, what it does, and an example.

# 1. dot append() method

# * Adds an element to the end of the list

fruits = ["apple", "banana"]
fruits.append("Cherry")
print(fruits) # Output: ["apple", "banana", "cherry"]


# 2. dot insert() method
#  * Inserts an element at a specific position

fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

# 3. dot extend() method

# * Adds elements from another list (or iterable) to the end.

fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)


# 4. dot remove() method

# * Remove the first occurence of a splendid value.

fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# 5. dot pop() method
#  * Removes and returns the element at a given index(default: last)

fruits = ["apple,", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# 6. dot clear() method
# * Removes all elements from list

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# 7. dot index() method
#  * Returns the index of the first occurence of a value

fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)

# 8. dot count() method
#  * Counts how many times a value appears 

fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))

# 9. dot sort() method
#  * Sorts the list in ascending order 9 (default)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# 10. dot reverse() method
#   * Reverses the order of the list

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

# 11. copy()
#  * Returns a shallow copy of the list( This should be familar already)
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)



