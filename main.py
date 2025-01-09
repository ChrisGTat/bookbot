def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number = word_count(text)
    characters = character_count(text)
    print(f"There are {number} words found in document")
    print(characters)

def book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)
    
def character_count(text):
    character_counts = {}
    lower_text = text.lower()
    for character in lower_text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

main()