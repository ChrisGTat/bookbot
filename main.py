def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number = word_count(text)
    letters = letter_count(text)
    print(f"There are {number} words found in document")
    print(letters)

def book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)
    
def letter_count(text):
    letter_total = {}
    lower_text = text.lower()
    for word in lower_text:
        for letter in word:
            if letter in letter_total:
                letter_total[letter] += 1
            else:
                letter_total[letter] = 1
    return letter_total

main()