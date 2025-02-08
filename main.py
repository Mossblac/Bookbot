def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report_list(chars_dict)
    
    


    header = f"--- Begin report of {book_path} ---"
    words_found_sentence = f"{num_words} words found in the document"
    print(header)
    print(words_found_sentence)
    print()
    print('\n'.join(report))
    print("--- End Report ---") 

def get_report_list(dict):
    report_list = []
    for key, value in dict.items():
        if key.isalpha():
            report_list.append(f"The '{key}' character was found {value} times")
    return report_list
    
   

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

    