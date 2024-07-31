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
    word_frequencies = count_word_frequency(file_contents)
    most_common_word, most_common_word_count = find_most_common_word(word_frequencies)
    char_count = count_characters(file_contents)
    sorted_characters = sort_characters(char_count)

    print(f"--- Begin report of {file_path} ---")
    print()
    print(f"{word_count} words found in the document")
    print()
    print(f"The most common word is '{most_common_word}' which was found {most_common_word_count} times")
    print()

    print("Characters found:")
    for item in sorted_characters:
        print(f"The '{item['character']}' character was found {item['num']} times")
    print()
    print("--- End report ---")

main('books/frankenstein.txt')