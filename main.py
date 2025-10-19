import sys
from stats import num_words_in_string, count_characters, sorted_dict_list

#Given a file, read the contents and return as a string
def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#main function to check input values, call functions to read, convert and format output to print word and character counts
def main():
    #exit the program if no input file provided
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    char_count = {}
    sorted_char_count = {}
    rel_path = sys.argv[1]
    #turn file contents to string
    book_content = get_book_text(rel_path)
    #get the word count in the book
    count_words = num_words_in_string(book_content)
    #get the character count in the book
    char_count = count_characters (book_content)
    #get sorted dictionary of the output
    sorted_char_count = sorted_dict_list(char_count)
    #pretty print of everything on bookbot
    print("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f'Found {count_words} total words')
    print ("--------- Character Count -------")
    #print only alphabetic items
    for item in sorted_char_count:
        if item[0].isalpha():
            print (f'{item[0]}: {item[1]} ' )
        else:
            continue
    print ("============= END ===============")

main()
