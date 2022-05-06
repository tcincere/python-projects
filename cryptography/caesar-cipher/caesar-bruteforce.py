'''
Filename: caesar-bruteforce.py
Function: Bruteforce text encrypted with the mono-alphabetic cipher, using a wordlist or via 'dumb' bruteforce.
Output: Print decrypted ciphertext, shift value and string match [--smart].

by: tcincere [https://github.com/tcincere]
'''

# Import appropriate modules.
import string
import argparse

# Colour definitions.
RED   = "\033[1;31m"  
YW    = "\033[1;93m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RST   = "\033[0;0m"


# Define argument parse. Set the description and epilogue when help menu is evoked.
parser = argparse.ArgumentParser (
    
    description="Caesar cipher brute-force program, using a wordlist to find relevant plain-texts.",
    epilog="by: tcincere [https://github.com/tcincere]"
    
)

# Add argument --smart, to provide user choice (dumb or smart bruteforce).
parser.add_argument (
    
    '-s', '--smart',
    help="Bruteforce, smartly, to find relevant plaintexts using a wordlist",
    action="store_true",
    default=False
    
)

# Parse the arguments.
args = parser.parse_args()

# Set ascii letters as variables [ease of use].
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

# Ask user for encrypted cipher-text.
ciphertext = input("Enter cipher-text: ")   


# Bruteforce function definition, ciphertext (string parameter).
def bruteforce(ciphertext):
    
    for shift in range(1, 26):
        plaintext = ""    
        
        for char in ciphertext:    
            
            if char.isupper():
                index = ((uppercase.find(char) - shift) % 26)
                plaintext += (uppercase[index])
            
            elif char.islower():
                index = ((lowercase.find(char) - shift) % 26)
                plaintext += (lowercase[index])
                        
            else:
                plaintext += char
        
        #Call function to find most relevant plaintexts.
        if args.smart == True:
            find_string(plaintext, shift)
        
        else:          
            print()
            print(f"{CYAN}shift: {RED}{shift}\n{YW}{plaintext}{RST}")


#Define find_string function.
def find_string(plaintext, shift):
    
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
                    print(f"{CYAN}shift: {RED}{shift}  {CYAN}match: {GREEN}<{word}>")
                    print(f"{YW}{plaintext}{RST}")
                    print()
                    
                    break
            else:
                continue
    

#Call function.
bruteforce(ciphertext)

