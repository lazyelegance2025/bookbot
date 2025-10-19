#function to take a string and return number of words
def num_words_in_string(input_text):
    total_words = input_text.split()
    return len(total_words)

#function to take a string and return character count in a dictionary
def count_characters (book_string):
    dict_to_return = {}
    book_string = book_string.lower()
    for char in book_string:
        if char in dict_to_return:
            dict_to_return[char] += 1
        else:
            dict_to_return[char] = 1
    return dict_to_return

#function to sort and return the dictionary by value in descending order
def sorted_dict_list(char_dict):
    sorted_dict = {}
    sorted_dict = sorted(char_dict.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))
    return sorted_dict