import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
letters_dict = {letter:code for (letter,code) in data.values}

word = input('enter a word: ').upper()
list_of_letters = [letters for letters in word]

for letter in list_of_letters:
    print(f"{letter} for {letters_dict[letter]}")