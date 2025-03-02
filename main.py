from stats import count_words, dictionary_of_letters, sort_dictionary
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py books/frankenstein.txt")
    sys.exit(1)

def main():
    book = get_book_text(sys.argv[1])
    amount_of_words = count_words(book)
    dictionary = dictionary_of_letters(book)
    sorted_dictionary = sort_dictionary(dictionary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {amount_of_words} total words")

    print("--------- Character Count -------")
    for dictionary in sorted_dictionary:
        if dictionary[0].isalpha():
            print(f'{dictionary[0]}: {dictionary[1]}')

def get_book_text(path_to_file):     
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

main()