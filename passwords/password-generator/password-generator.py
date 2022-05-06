'''
Filename: password.py
Function: Create passwords of length specified by user.

by: tcincere [https://github.com/tcincere]
'''

import argparse
from string import ascii_letters
from random import randint

parser = argparse.ArgumentParser(
    
    description="Password generator of length specified by user.",
    epilog="by: tcincere [https://github.com/tcincere]"
    
)

parser.add_argument(
    
    "-l", "--length",
    metavar="length",
    type=int,
    help="Length of password to generate [default: 20]",
    action="store",
    dest="length",
    default=20,
    required=False
    
)

parser.add_argument(
    
    "-q", "--quantity",
    metavar="quantity",
    type=int,
    help="Number of passwords to generate [default: 1]",
    action="store",
    dest="quantity",
    default=1,
    required=False
    
)

# Variable initialisation.

GREEN = "\033[1;32m"
WHITE = "\033[1;40m"
YELLOW = "\033[1;33m"
RST = "\033[0;0m"

args = parser.parse_args()

length = args.length
quantity = args.quantity
letters = ascii_letters

# Special character variables.
special_characters = "?@[/]^_#$%&"
special_characters_length = len(special_characters) - 1


def generate_password(length, quantity):
       
    count = 0
    while count < quantity:
    
        password = ""
        
        while len(password) < length:
        
            index = (randint(0, 51))
            letter = str(letters[index])
            password += letter
        
            number = randint(1, 9)
            password += str(number)
        
            special_char_index = (randint(1, special_characters_length))
            password += (special_characters[special_char_index])
        
        shorten(password, length, count)
        count += 1


def shorten(password, length, count):
    
    if len(password) > length:

        subtract = int(len(password) - length)
        password = password[subtract:]
        print(f"{GREEN}{count}{RST}.{WHITE} {password}")

    else:

        print(f"{GREEN}{count}{RST}.{WHITE} {password}")
      

# Output.
print(f"\n\t{YELLOW}PASSWORDS{RST}")
print(f"{WHITE}    -----------------\n")
generate_password(length, quantity)
print()
