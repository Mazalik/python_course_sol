import sys
import functions_count_from_text 

def main():
    if len(sys.argv) != 2:
        exit(f"The correct usage is: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()

    characters = functions_count_from_text.count_characters(text)
    lines = functions_count_from_text.count_lines(text)
    words = functions_count_from_text.count_words(text)
    print(f"This file contains {characters} characters, {lines} lines, and {words} words.")

main()
