# This script processes a text document and prints a word count and letter occurance count.
# The letter occurance count is in order or frequency and thus requires funtion to make.
# The intended order; file is retrieved and read, the word count (number) is logged, -
# - Each word is split into characters and only letters are then counted in a directory, -
# - that directory is sorted into decending order of frequency, a report is generated from that.
# Main should then print the word count and report.
def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number = word_count(text) 
    letters = letter_count(text)
    letters_sorted = sort_letters(letters)
    report = report_maker(letters_sorted)
    print(f"There are {number} words found in document\n")
    print(report)
    print("###---End of Report---###")

def book_text(path_to_file): # Used to read the file
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text): # Word count (Techically not a word counter tbh)
    words = text.split()
    return len(words)
    
def letter_count(text): # The letter counter.
    letter_counts = {}
    lower_text = text.lower() # This is used to make everything lower-case
    for character in lower_text:
        if character.isalpha() == True: # This is used to check is charcter is a letter.
            if character in letter_counts: # Will add to the directory or create a new key : value pair
                letter_counts[character] += 1
            else:
                 letter_counts[character] = 1
    return letter_counts

def sort_letters(letters): # The letters directory is sorted by most frequent here.
    unsorted_list = [] # The letters directory has to be a list of smaller directories for the sort function to work.
    for letter in letters: # For each key (now given the variable 'letter') in the given directory
        num = letters[letter] # For the value of the key (now called letter)
        letter_list = {"letter":letter,"num":num} # A distict directory is created labelling the key:value pair are letter:num
        unsorted_list.append(letter_list) # The single letter directory is added to the list.
# We have to use the built-in .sort function, it defaults to ascending order and thus needs reserve=True in this case.
# The .sort function also needs a comparison key and uses a seperate function for this.
    unsorted_list.sort(reverse=True, key=num_check)
    sorted = unsorted_list #This is here just for extra clarity.
    return sorted
    

def num_check(unsorted_letter):
    return unsorted_letter["num"] #This specifies that the value being compared is the num value of a letter in the directory list.

def report_maker(letters_sorted):
    report = ""
    for i in letters_sorted:
        report += f"The letter '{i["letter"]}' appears {i["num"]} times. \n"
    return report



main()