from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report_list(chars_dict)
    sorted_report = sort_by_int_in_sentence(report)
    
    


    header = f"-- Begin report of {book_path} --"
    words_found_sentence = f"{num_words} words found in the document"
    print(header)
    print(words_found_sentence)
    print()
    print('\n'.join(sorted_report))
    print("--- End Report ---") 

def sort_by_int_in_sentence(sentences):
    def get_int_from_sentence(sentence):
        for word in sentence.split():
            if word.isdigit():
                return int(word)
        return 0    
    
    sentences.sort(reverse=True, key=get_int_from_sentence)
    return sentences

def get_report_list(dict):
    report_list = []
    for key, value in dict.items():
        if key.isalpha():
            report_list.append(f"'{key}: {value}'")
    return report_list



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

    