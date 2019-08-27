"""Program that asks for strings until an empty string is entered, and returns duplicate strings"""

def main():
    string_list = []
    duplicate_strings = []
    input_string = str(input("Enter a string: ")).lower()
    if input_string != "":
        string_list.append(input_string)
    while input_string != "":
        input_string = str(input("Enter another string: ")).lower()
        if input_string != "":
            if input_string in string_list and input_string not in duplicate_strings:
                """check if string already entered and if string is already duplicate"""
                duplicate_strings.append(input_string)
            else:
                string_list.append(input_string)
    if not duplicate_strings:
        print("No duplicate strings entered")
    else:
        print("Duplicate Strings: ")
        for duplicate in duplicate_strings:
            print(duplicate)


main()