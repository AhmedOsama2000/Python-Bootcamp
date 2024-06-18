import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Convert the data frame into a dictionary
# row.letter is the letters of the alphabet
# row.code is the acronym of the letter
nato_dict = {value.letter: value.code for (letter, value) in nato_file.iterrows()}

word = list(input("Enter a word: ").upper())

# TODO 2. Create a list of the phonetic code words from a word the user inputs.
word_list = [nato_dict[letter] for letter in word]

print(word_list)
