import string



def read_book(book_path):
    # use with to open a "book" saved in a text file
    # path to file is relative to where the program is being run from
    with open(book_path) as f:
        return f.read()

def word_count(book):
    book_as_string = book.split()
    return len(book_as_string)

def lower_string(book_path):
    return read_book(book_path).lower()

def count_each_ascii(book):
    dictonary_of_all_char_in_book = {}
    for char in book:
        if char in dictonary_of_all_char_in_book:
            dictonary_of_all_char_in_book[char] += 1
        else:
            dictonary_of_all_char_in_book[char] = 1

    return dictonary_of_all_char_in_book

def main():
    dicto = count_each_ascii(lower_string("books/frankenstein.txt"))
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(read_book("books/frankenstein.txt"))} words found in the document")
    print("")
    for char in string.ascii_lowercase:
        print(f"The '{char}'  character was found {dicto[char]} times")
    print("--- End report ---")

main()