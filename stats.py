def count_characters(text):
    lowered_text = text.lower()
    char_counts = {}

    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def get_sort_key(dictionary):
    return dictionary["num"]

def sort_char_dict(char_counts_dict):
    char_list = []

    for char, num in char_counts_dict.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(key=get_sort_key, reverse=True)
            
    return char_list