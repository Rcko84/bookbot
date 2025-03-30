import sys

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_list(char_count)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

from stats import get_num_words, count_characters, sort_list
 

main()