# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("Enter a text: ")
anagram = input("Enter a text: ")


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()

    # sort the word
    word = sorted(word)
    anagram = sorted(anagram)

    if len(word) != len(anagram) or word != anagram:
        return False
        
    return True

print(find_anagram(word, anagram))