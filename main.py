def char_count(file_contents):
    word_dict = {}
    for char in file_contents:
        if char.isalpha():
            if char in word_dict:
                word_dict[char] += 1 
            else:
                word_dict[char] = 1
    return word_dict


def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

    words = file_contents.split()

    word_count = 0
    for word in words:
        word_count += 1

    print(word_count)

    word_dict = char_count(file_contents)
    word_list = list(word_dict.items())
    word_list.sort()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for key, count in word_list:
        print(f"The '{key}' character was found {count} times")

main()



