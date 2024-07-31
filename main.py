import sys

def count_words(text):
    words = text.split()
    return len(words)

def count_word_frequency(text):
    word_count = {}
    words = text.lower().split()
    for word in words:
        if len(word) > 1 or word in ['i', 'a']:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

def find_most_common_word(word_count):
    most_common_word = None
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            most_common_word = word
            max_count = count
    return most_common_word, max_count

def count_characters(text):
    char_count = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_characters(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"character": char, "num": count})
    
    def sort_on(dict_item):
        return dict_item["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def count_punctuation(text):
    punctuation_count = {}
    for char in text:
        if not char.isalpha() and not char.isspace() and not char.isdigit():
            if char in punctuation_count:
                punctuation_count[char] += 1
            else:
                punctuation_count[char] = 1
    return punctuation_count

def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return

    word_count = count_words(file_contents)
    word_frequencies = count_word_frequency(file_contents)
    most_common_word, most_common_word_count = find_most_common_word(word_frequencies)
    char_count = count_characters(file_contents)
    sorted_characters = sort_characters(char_count)
    punctuation_count = count_punctuation(file_contents)

def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return

    word_count = count_words(file_contents)
    word_frequencies = count_word_frequency(file_contents)
    most_common_word, most_common_word_count = find_most_common_word(word_frequencies)
    char_count = count_characters(file_contents)
    sorted_characters = sort_characters(char_count)
    punctuation_count = count_punctuation(file_contents)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    
    if most_common_word:
        print(f"The most common word is '{most_common_word}' which was found {most_common_word_count} times.")
    else:
        print("No common word found.")

    print("\nCharacter frequency (descending order):")
    for item in sorted_characters:
        print(f"Character '{item['character']}' is found {item['num']} times.")

    print("\nPunctuation/Symbol frequency:")
    for punctuation, count in punctuation_count.items():
        print(f"'{punctuation}': {count}")

    print("--- End of report ---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)