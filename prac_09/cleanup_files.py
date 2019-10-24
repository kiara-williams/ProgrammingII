"""
CP1404/CP5632 Practical
File Cleanup Program
"""

import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for i, char in enumerate(filename):
        if i == 0 and (char.islower() or char.isupper()):
            char = char.upper()
            new_name += char
        # This section is problematic for files that are already spaced and capitalised
        elif char.isupper():
            new_name = new_name + "_" + char
        elif char == " ":
            new_name += "_"
        elif char == "_":
            pass
        else:
            new_name += char
    return new_name


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for file in filenames:
            file_name = os.path.join(directory_name, file)
            new_name = os.path.join(directory_name, get_fixed_filename(file))
            os.rename(file_name, new_name)


main()
