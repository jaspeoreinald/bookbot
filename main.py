import sys  # Step 2: Import the sys module
from stats import count_characters, sort_char_dict

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    words_list = text.split()
    return len(words_list)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    try:
        book_content = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        print("Please check the path and try again.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: '{book_path}' is a directory, not a file.")
        print("Please provide a path to a text file.")
        sys.exit(1)
        
    num_words = count_words(book_content)
    char_counts = count_characters(book_content)
    sorted_char_list = sort_char_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_char_list:
        char = item["char"]
        num = item["num"]
        
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")


main()