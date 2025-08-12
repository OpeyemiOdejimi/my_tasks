# Python data structure
# 1.String _ immutable sequence of characters(often treated like a sequence)
# 2. Tuple - ordered, immutable sequence
# 3. Set - unordered collection of unique items
# 4. Dict(dictionary/map) - key - value mapping
# 5. List - ordered, mutable sequence
# 6. Also: range, bytes/bytearray,and useful types from collections (namedtuple,defaultdict, Counter, deque)


#1. String in Pythons
# * A string in pyhon is a sequence of characters enclosed in either single quotes, double quotes or triple quotes
# * Strings are used to store text data like names, sentences, or any combination of letters, numbers, and symbols

# Single quotes
# name = 'Ada'

# DOuble quotes
# greeting = "Hello"

# Triple quotes (for multi-line strings)
# story = '''Once upon a time,
# there was a coder named Ada.'''

# String with numbers and symbols
# password = "p@ssword123"

# print(password)
# print(name)
# print(greeting)

# Explanation
# * Single quotes ' and double quotes " work the same way
# * Triple quotes allow your string to span across multiple lines without using \n
# * Strings can contain letters, numbers, spaces, and special characters
# > Tip: In Python, there's no "character" type - even a single letter is considered a string.

# String Operations

# Indexing

# word = "Python"
# print(word[0])  # P
# print(word[-1]) # n

# Slicing

# word = "Python"
# print(word[0:4]) # Pyth
# print(word[2:]) # thon
# print(word[:3]) # Pyt
# print(word[::2]) # Pto
# print(word[::-4])

# String Concatenation and Repetition

# Concatenation

# a = "Hello"
# b = "World"
# print(a + " " + b) # Hello World

# Repetition

# word = "Hi! "
# print(word * 3) # Hi! Hi! Hi!

# String Searching and Checking

# Membership

# text = "Python programming"
# print("Python" in text) # True
# print("Java" not in text) # true

# find() /rfind()

# text = "Hello World"
# print(text.find("o")) # 4
# print(text.rfind("o")) # 7

# index() / rindex()
# * (Like find() but raises an error if not found)

# text = "Hello World"
# print(text.index("World")) # 6

# startswith() / endswith()
# filename = "data.csv"
# print(filename.startswith("data")) # True
# print(filename.endswith(".csv")) # True
# print(filename.endswith(".Messi"))

# String Methods

# * Creating and manipulating strings
#   * upper()
#   * lower()
#   * title()
#   * strip()
#   * replace()
#   * capitalize()
#   * swapcase()
#   * strip()
#   * lstrip()

# upper()
# * Converts all chacters in the string to uppercase

# name = "Ada Balogun"
# print(name.upper())

# lowercase()

# *Converts all characters in the string to lowercase

# sentence = "PYTHON IS AMAZING"
# print(sentence.lower())

# strip()
# * Removes whitespaces (or specified characters) from both ends of the string.

# text = "   Abuja   "
# print(text.strip())

# replace 
# * replaces occurences of a substring with another substring

# message = "I love Java"
# print(message.replace("Java", "Python"))

# swapcase()
# * Switches lowercase to uppercase and vice versa

# text = "Hello ABEOKUTA"
# print(text.swapcase())

# Istrip()
# * Removes whitespaces (or specified characters) from the left side only.

# text = "    Nigeria"
# print(text.lstrip)

# rstrip()
# Removes whitespace (or specified characters) from the right side only.

# text = "Nigeria    "
# print(text.rstrip())


# split()
# * Splits a string into a list using a separator (default is space)
# fruits = "mango orange banana"
# print(fruits.split())

# rsplit()
# * Splits a string into a list from the right side

# text = "one, two, three, four"
# print(text.rsplit(",", 2))

# splitlines()
# * SPlits a string into a list at each newline (\n)

# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())

# join()
# * Joins a list of strings into onr string with a specified separator

# words = ["I", "love", "Python"]
# print (" ".join(words))

# center()
# * Centers the string with a speicified with, padding with spaces or characters.

# text = "Python"
# print(text.center(20, "_"))

# Ijust()
# * Left-aligns the string within a specified width, padding with spaces or characters.

# text = "Python"
# print(text.ljust(10, "*"))

# rjust()
# * Right-aligns the string within a specified width, padding with spaces or characters.

# text = "Python"
# print(text.rjust(10, "*"))

# zfill()
# Pads a numeric string on the left with zeros until it reaches a given length.

# nums = "42"
# print(nums.zfill(5))

# isalpha()
# * Checks if the string contains only letters

# print("Lagos".isalpha())  # True
# print("Lagos123".isalpha())  # False

# isdigit()
# * Checks if the string contains onluy digits.

# print("12345".isdigit())  # True
# print("123a".isdigit())  # False

# isalnum()

# * checks if the string contains only letters and digits.

# print("python3".isalnum()) # True
# print("Python 3".isalnum()) # True