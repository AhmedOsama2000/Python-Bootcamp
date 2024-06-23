import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Convert the data frame into a dictionary
# row.letter is the letters of the alphabet
# row.code is the acronym of the letter
nato_dict = {value.letter: value.code for (letter, value) in nato_file.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word the user inputs.
is_on = True
while is_on:
    word = list(input("Enter a word: ").upper())
    if word == "quit":
        break
    else:
        try:
            word_list = [nato_dict[letter] for letter in word]

        except KeyError:
            print("Sorry, Only letters are accepted")

        else:
            print(word_list)
