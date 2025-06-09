import sys
from stats import count_words, count_characters, sort_dict_by_value, print_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath:str) -> str:
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    frankenstein_text = get_book_text(path_to_book)
    word_count = count_words(frankenstein_text)
    sorted_char_count = sort_dict_by_value(count_characters(frankenstein_text))
    print_report(path_to_book, word_count, sorted_char_count)

if __name__ == "__main__":
    main()
