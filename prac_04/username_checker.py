"""Program that asks a user for their username and checks it against an existing list"""

def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = str(input("Enter your username"))
    if user_input in usernames:
        print("Access granted.")
    else:
        print("Access denied")

main()