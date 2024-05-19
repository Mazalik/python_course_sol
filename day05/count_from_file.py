import sys
import FunctionsCountFromText 

def main():
    if len(sys.argv) != 2:
        exit(f"The correct usage is: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()

    characters = FunctionsCountFromText.count_characters(text)
    lines = FunctionsCountFromText.count_lines(text)
    words = FunctionsCountFromText.count_words(text)
    print(f"This file contains {characters} characters, {lines} lines, and {words} words.")

main()
