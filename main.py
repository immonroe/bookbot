def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    lowered_string = text.lower()
    for i in lowered_string:
        if i.isalpha():
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
    return char_count

def sort_characters(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"character": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def main(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_characters = sort_characters(char_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_characters:
        print(f"The '{item['character']}' character was found {item['num']} times")

    print("--- End report ---")

main('books/frankenstein.txt')