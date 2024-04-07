def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    

    letters = [count_letters(text)]

    tmp_list = letters_list(count_letters(text))
    tmp_list.sort(reverse=True, key=sort_on)
    #print(tmp_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(f"")

    for single_letter in tmp_list:
        print(f"The {single_letter["name"]} character was found {single_letter["num"]} times")
    print("--- End report ---")
    


def count_words(text):
    words = text.split()
    return (len(words))

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_letters(text):
    lower_text = text.lower()
    sorted_letters = {}
    letters_list = []

    for letter in lower_text:
        if letter in sorted_letters:
            sorted_letters[letter] += 1
        else:
            sorted_letters[letter] = 1
        
    return sorted_letters

def letters_list(dict):
    letters_list = []
    new_dict = {}
    for letter in dict:
        if letter.isalpha():
            new_dict = {"name": letter, "num": dict[letter]}
            letters_list.append(new_dict)

    return letters_list

    
def sort_on(dict):
    return dict["num"]








main()
