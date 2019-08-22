"""Program that converts characters to ascii and vice versa."""

LOWER = 33
UPPER = 127

def main():
    MENU = """ASCII Conversion
    Enter A to convert a character to ASCII
    Enter C to convert ASCII to a character
    Enter T to print an ASCII table
    Enter Q to quit"""
    print(MENU)
    selection = get_input()
    while selection != "Q":
        if selection == "A":
            character = str(input("Enter a character: "))
            char_code = ord(character)
            print("The ASCII code for {} is {}".format(character, char_code))
            print(MENU)
            selection = get_input()
        elif selection == "C":
            char_loop_sentinel = False
            while char_loop_sentinel == False:
                try:
                    char_code = int(input("Enter a number between {} and {}".format(LOWER, UPPER)))
                    if char_code >= LOWER and char_code <= UPPER:
                        character = chr(char_code)
                        print("The character for {} is {}".format(char_code, character))
                    else:
                        print("Invalid Option")
                except ValueError:
                    print("Invalid Option")
                char_loop_sentinel = True
                print(MENU)
                selection = get_input()
        elif selection == "T":
            for i in range(LOWER, UPPER,1):
                character = chr(i)
                print("| {:>3} | {:^3s} |".format(i, character))
            print(MENU)
            selection = get_input()
        else:
            print("Invalid Option. Please select from the menu")
            print(MENU)
            selection = get_input()
    print("Exiting application. Goodbye")


def get_input():
    """Requests input and normalises it"""
    selection = str(input("Enter your selection"))
    selection = selection.upper()
    return selection


main()