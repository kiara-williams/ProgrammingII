"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
MENU = """Enter "S" for standard substitution
Enter "W" for wildcard substitution
Enter "Q" to quit"""

print("This program will take a string of letters and use substitution to create a new string")
print(MENU)
selection = str(input("Choose an option")).upper()
while selection != "Q":
    word = ""
    if selection == "S":
        word_format = str(input("Enter a string of characters to substitute using a-z. \n>>>")).lower()
        for kind in word_format:
            if kind not in VOWELS:
                word += random.choice(CONSONANTS)
            else:
                word += random.choice(VOWELS)
            print(word)
            print(MENU)
            selection = str(input("Choose an option")).upper()
    elif selection == "W":
        word_format = str(input("Enter a string of characters using a-z. \nUse # for wildcard vowels and % for wildcard consonants. "
                                "\nUse other special characters for a random letter. \n>>>")).lower()
        for kind in word_format:
            if kind == "#":
                word += random.choice(VOWELS)
            elif kind == "%":
                word += random.choice(CONSONANTS)
            elif kind not in VOWELS and kind not in CONSONANTS:
                word += random.choice(VOWELS+CONSONANTS)
            else:
                word += kind
        print(word)
        print(MENU)
        selection = str(input("Choose an option")).upper()
    else:
        print("Invalid Option. Please select from the menu")
        print(MENU)
        selection = str(input("Choose an option")).upper()
print("Goodbye")