PASSWORD_LENGTH = 6

def main():
    password = get_password()
    print_password(password)
    print("\nYour password has been accepted")


def print_password(password):
    """Iterate through range of password length to print stars"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """Ask user for password input and checks password length against length constant"""
    print("Your password needs to contain at least {} characters".format(PASSWORD_LENGTH))
    password = str(input("Enter a password: "))
    while len(password) < PASSWORD_LENGTH:
        print("Your password needs to contain at least {} characters".format(PASSWORD_LENGTH))
        password = str(input("Enter a password"))
    return password


main()