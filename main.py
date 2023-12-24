def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_num_words(text)
    num_of_chars = get_chars(text)
    book_report = get_report(num_of_chars)
   # print(num_of_words, " words found in the document")
   # print("Character count: \n", num_of_chars)
    print(
        "--- Begin report of ",
        book_path,
        " ---\n",
        num_of_words,
        "words found in the document\n\n",
    )
    for char in book_report:
        ch = char[0]
        count = char[1]

        print(f"The '{ch}' character was found {count} times")
    print("--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    chars = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars

def get_report(num_of_chars):
    chars_list = list(num_of_chars.items())
    sorted_chars = sorted(chars_list, key=lambda x: x[1], reverse=True)
    
    return sorted_chars
main()