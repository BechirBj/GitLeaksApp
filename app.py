#import subprocess

#allowed_commands = {
 #   "date": ["date"],
  #  "whoami": ["whoami"],
#}

#user_input = input("Enter a command: ")

#if user_input in allowed_commands:
    # subprocess.run(allowed_commands[user_input], check=True)
 #   print("Hllo")
#else:
 #   print("Command not allowed")
#import subprocess

#user_input = input("Enter a command: ")
#subprocess.call(user_input, shell=True)
allowed_commands = {
    "date": ["date"],
    "whoami": ["whoami"],
}

user_input = input("Enter a command: ")

if user_input in allowed_commands:
    print("Command allowed")
else:
    print("Command not allowed")
