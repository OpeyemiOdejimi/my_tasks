# Ask the user to enter a sentence and print the number of vowels in it.

# que 9:
sentence = input("Enter a sentence: ")
numOfVowels= sentence.count("a") + sentence.count("e") + sentence.count("o") + sentence.count("i") + sentence.count("a")
print(numOfVowels)
