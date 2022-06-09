# Write a python program that counts and returns the number of words in a given text
# Input: "Hello World"
# Expected Output: 2
# get an input from the user
text = input("Enter a text: ");

def count_words(text):
    return len(text.split())

print(count_words(text))
