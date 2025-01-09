def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number = word_count(text)
    print(f"There are {number} words found in document")

def book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)
    

main()