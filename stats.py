def count_words(text: str) -> int:
    num_words = len(text.split())
    return num_words
    
def count_characters(text: str) -> int:
    count_dict = {}
    text_low = text.lower()
    word_list = text_low.split()
    for word in word_list:
        for char in word:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
    return count_dict

def sort_dict_by_value(d: dict) -> list:
    list_of_dicts = []
    for key, value in d.items():
        new_dict = {}
        new_dict['char'] = key
        new_dict['num'] = value
        list_of_dicts.append(new_dict)

    def sort_on(dict):
        return dict["num"]
    
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

def print_report(book_path:str, word_count:int, sorted_char_count: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")    
    print("---------- Character Count -------")
    for char_info in sorted_char_count:
        if char_info['char'].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")
    



        
        

        