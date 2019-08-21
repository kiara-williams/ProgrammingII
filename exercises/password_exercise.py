PASSWORD_LENGTH = 6
print("Your password needs to contain at least {} characters".format(PASSWORD_LENGTH))
password = str(input("Enter a password: "))
while len(password) < PASSWORD_LENGTH:
    print("Your password needs to contain at least {} characters".format(PASSWORD_LENGTH))
    password = str(input("Enter a password"))
for i in range(len(password)):
    print("*", end="")
print()
print("Your password has been accepted")