'''
File: affine-encrypt.py
Function: Encrypt plaintext with affine cipher

by: tcincere [https://github.com/tcincere]
'''

import argparse
import string


parser = argparse.ArgumentParser(
    
    description="Affine cipher - enter plaintext and output encrypted plaintext ciphertext.",
    epilog="by: tcincere [https://github.com/tcincere]"
)

alpha_key_choices = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


parser.add_argument(
    
    "-a", "--alpha-key",
    metavar="alpha",
    type=int,
    help="Alpha value - alpha and 26 (alphabet length) must be co-prime",
    choices=alpha_key_choices,
    default=5,
    dest="alpha_key"
)

parser.add_argument(
    
    "-b", "--beta-key",
    metavar="beta",
    type=int,
    help="Beta value - beta key must be in range 0-25",
    choices=range(0, 26),
    default=5,
    dest="beta_key"
)

args = parser.parse_args()

alpha_key = args.alpha_key
beta_key = args.beta_key

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

#Introductory text.
print()
print("\t--------------")
print("\tAFFINE CIPHER")
print("\t--------------")
print()

plaintext = input("Enter plain-text: ")


def affine_encrypt(alpha_key, beta_key):
    
    ciphertext = ""
    for char in plaintext:
        
        if char.isupper():
            index = ((uppercase.find(char) * alpha_key) + beta_key) % 26
            ciphertext += uppercase[index]
        
        elif char.islower():
            index = ((lowercase.find(char) * alpha_key) + beta_key) % 26
            ciphertext += lowercase[index]
        
        else:
            ciphertext += char

    print(ciphertext)
    

affine_encrypt(alpha_key, beta_key)
