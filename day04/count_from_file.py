import sys

def main():
    if len(sys.argv) != 2:
        exit(f"The correct usage is: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()

    characters = count_characters(text)
    lines = count_lines(text)
    words = count_words(text)
    print(f"This file contains {characters} characters, {lines} lines, and {words} words.")

def count_characters(text):
    return len(text)

def count_lines(text):
    lines_list = text.split("\n") 
    return len(lines_list)

def count_words(text):
    words_list = text.split() 
    return len(words_list)

main()
