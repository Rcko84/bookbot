def get_num_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_characters(book_text):
    char_count = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    
def sort_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list