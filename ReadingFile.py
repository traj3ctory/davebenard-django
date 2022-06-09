# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    # read the file content
    with open(filename, "r") as f:
        content = f.read()
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # count the occurrence of words in that text
    return {word: text.count(word) for word in text.split()}

print(count_words())