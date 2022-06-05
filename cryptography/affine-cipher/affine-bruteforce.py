'''
Filename: affine-bruteforce.py
Function: Bruteforce cipher-text encrypted with the affine cipher.

by: tcincere [https://github.com/tcincere]
'''

import argparse
import string
import math

# Colour definitions.
RED   = "\033[1;31m"  
YW    = "\033[1;93m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
MAGENTA = "\033[35m"
RST   = "\033[0;0m"

parser = argparse.ArgumentParser(
    
    description="Affine bruteforce program - brute ciphertext using a wordlist",
    epilog="by: tcincere [https://github.com/tcincere]"
)

parser.add_argument(
    
    "-s", "--smart",
    #metavar=avar="smart",
    help="Bruteforce, smartly, to find relevant plaintexts using a wordlist",
    action="store_true",
    default=False
    
)

args = parser.parse_args()

# Set ascii letters as variables [ease of use].
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

print()
print("\t-------------------------")
print("\tAFFINE CIPHER BRUTEFORCE")
print("\t-------------------------")
print()

ciphertext = input("Enter cipher-text: ")



def bruteforce(ciphertext):
    
    for alpha_key in range(1, 26):
        gcd = math.gcd(alpha_key, 26)
        
        if gcd == 1:
            alpha_inverse = pow(alpha_key, -1, 26)      
            
            for beta_key in range(0, 26):
                plaintext = ""
                for char in ciphertext:
                
                    if char.isupper():
                        index = ((uppercase.find(char) - beta_key) * alpha_inverse) % 26
                        plaintext += uppercase[index]
                    
                    elif char.islower():
                        index = ((lowercase.find(char) - beta_key) * alpha_inverse) % 26
                        plaintext += lowercase[index]
                    
                    else:
                        plaintext += char
    
                if args.smart == True:
                    find_string(plaintext, alpha_key, beta_key)
                else:
                    print()
                    print(f"{CYAN}A: {alpha_key}, {RED}B: {beta_key}")
                    print(f"{YW}{plaintext}")


def find_string(plaintext, alpha_key, beta_key):
    
	# File opening error-handling.
    try:
        open("common-words.txt", "r")
    except FileNotFoundError as e:
        print(e)
	
     
    with open("common-words.txt", "r") as file:
        
        for word in file:
            if len(word) > 4:
                #Remove new line from each line.
                word = word.strip()
                
                #Case insensitive sub-string search.
                if word.casefold() in plaintext.casefold():
                    print()
                    print(f"{CYAN}A: {alpha_key}  {MAGENTA}B: {beta_key} {RED} match: {GREEN}<{word}>")
                    print(f"{YW}{plaintext}")
                    break
            else:
                continue


print("\n\tRESULTS")
print("    ---------------")
bruteforce(ciphertext)