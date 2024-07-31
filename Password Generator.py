#Ask user if they want to generate a password
# If yes, ask for password length
# Generate password
# Print password

import string
import random

characters = list(string.ascii_letters + string.digits +"@#$%^&*()")

def generate_password():
    password_length = int(input("Input desired password length: "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Would you like to generate a password?")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended")
else:
    print("Invalid, please type yes or no")
    quit()
