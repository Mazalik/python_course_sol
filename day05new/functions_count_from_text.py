def count_characters(text):
    return len(text)

def count_lines(text):
    if text != "":
        lines_list = text.split("\n") 
        return len(lines_list)
    else:
        return 0

def count_words(text):
    words_list = text.split() 
    return len(words_list)