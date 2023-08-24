# Imports
from functools import cache
import random


# Variables
password_to_guess = "!"
password_to_check = ""
password_status = False
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
common_password_punctuation = [".", "?", "!", "$", "*", ",", "-", "_"]



# Opening this file is completely optional. Removing line 17 & the last line will save storage & won't negatively effect the code.
with open("Passwords_checked.txt", "a") as file:
    # Infinitely loops.
    while True:
        # Checks if the current random password is the password 
        if password_to_check == password_to_guess:
            # Ends the loop if true
            break
        else:
            # If the random password character length is over 8
            if len(password_to_check) > 1:
                # The random password will reset to an empty string
                password_to_check = ""
            else:
                # Otherwise it will get a random choice, letters, numbers or punctuation
                # Then it will append a random character within the random character set
                password_to_check+=f"{random.choice([random.choice(letters), random.choice(numbers), random.choice(common_password_punctuation)])}"
        # Writes the current random password to a file.
        # This is pure bloatware and should be removed if you dont have a good device that can handle a large file.
        file.write(f"\n------------------------------\nChecking: {password_to_check}")
    print(f'Found the password! The password is inside the quotations: "{password_to_check}"')
