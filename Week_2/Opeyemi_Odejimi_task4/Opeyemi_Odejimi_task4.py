# Task 4
# 1. Your Favourite Life Quote
#   * Ask the user to input their favourite quote.
#   * Convert it to title case
#   * Print it with quotation marks using escape sequences.

quote = input("What is your favorite quote?: ")
titleCase = quote.title()
print(f"I love this Quote - \"{titleCase}\"")


# 2. Shopping List Manager
#   * Create an empty list
#   * Ask the user to enter 3 shopping items (one by one).
#   * Add them to the list
#   * Display the list as a single string, separated by commas.

empty_list = []
empty_list_1 = input("Enter choosen item 1: ")
empty_list_2 = input("Enter choosen item 2: ")
empty_list_3 = input("Enter choosen item 3: ")
add_list = [empty_list_1, empty_list_2, empty_list_3]
print(", ".join(add_list))


# 3. Word Counter
#   * Ask  the user for a sentence.
#   * Print how many words are in the sentence.

sentence = input("Kindly enter a sentence: ")
wordCount = sentence.split()
print(len(wordCount))


# 4. Name Organizer
#   * Ask the user to enter 5 names (separated by spaces)
#   * Convert all names to lowercase
#   * Sort the list alphabetically
#   * Display them one name per line. - Tips: use range(), sort(), for, in, split(), len(), lower()


names = input("Enter 5 names separated by space: ")
convert = names.lower()
convert_all_names = convert.split()
convert_all_names.sort()
for name in convert_all_names:
     print(name)


# 5. Student Score Tracker
#   * Ask the user for 3 student name
#   * For each student, ask for their score
#   * Store the results in two lists (one for names, one for scores)
#   * Print a formatted output showing Name -- Score, aligned neatly.
#       - Tips: You are to start by creating two empty lists

nameList = []
scoreLlist = []
studentNames = input("Input 3 student names separated by space: ")
newStudentNames = studentNames.split()
student1 = input(f"Input {newStudentNames[0]} score: ")
student2 = input(f"Input {newStudentNames[1]} score: ")
student3 = input(f"Input {newStudentNames[2]} score: ")
studentScoreList = [student1, student2, student3]

print("Student Score Table")
print(f"{newStudentNames[0]}\t- {studentScoreList[0]}")
print(f"{newStudentNames[1]}\t- {studentScoreList[1]}")
print(f"{newStudentNames[2]}\t- {studentScoreList[2]}")


# 6. Word Analyzer
#   * Ask the user to input a word
#   * Print the length of the word
#   * Check if it is all uppercase, all lowercase, or title case
#   * Reverse the word using slicing

word = input("Please enter a word of choice: ")
print(len(word))
in_upper_case  =  word.isupper()
print(f"The word entered is in upper_case: {in_upper_case}")
in_lower_case  =  word.islower()
print(f"The word entered is in lower_case: {in_lower_case}")
in_title_case  =  word.istitle()
print(f"The word entered is in title_case: {in_title_case}")
print(word[::-1])


# 7. List Manipulation
#  * Create a list of five cities
#  * Replace the third city with a new one (entered by the user)
#  * Remove the last city
#  * Add a new city to the beginning of the list
#  * Print the updated list.

name_of_cities = ["Lagos", "Kano", "Ibadan", "Abeokuta", "Calabar"]
print(name_of_cities)
replace_city = input("Enter a new city")
name_of_cities[2] = replace_city
name_of_cities.remove("Calabar")
name_of_cities.insert(0, "Gwagwalada")
print(name_of_cities)