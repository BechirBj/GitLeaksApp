allowed_commands = {
    "date": ["date"],
    "whoami": ["whoami"],
}

user_input = input("Enter a command: ")

if user_input in allowed_commands:
    print("Command allowed")
else:
    print("Command not allowed")
