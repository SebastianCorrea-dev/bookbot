def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")

def count_characters(path_to_file):
    character_dict = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        for char in file_contents.lower():
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    
    return character_dict
def sort_on(dict):
    return dict["count"]
def print_count(character_dict, path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    get_num_words(path_to_file)
    print("--------- Character Count -------")
    list_of_dictionaries = []
    for key in character_dict:
        new_dict = {"char": key, "count": character_dict[key]}
        list_of_dictionaries.append(new_dict)
    
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    for dictionary in list_of_dictionaries:
        character = dictionary["char"]
        count = dictionary["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")
    return