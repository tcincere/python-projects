
import argparse
import string


parser = argparse.ArgumentParser (
    
    description="Shift cipher - enter plaintext and a shift to output encrypted cipher-text.",
    epilog="by: tcincere [https://github.com/tcincere]"
    
)

parser.add_argument (
    
    "-s", "--shift",
    metavar="shift",
    type=int,
    choices=range(1, 26),
    help="Value to shift letters [default: 13]",
    default=13,
    dest="shift"
    
)

args = parser.parse_args()
shift = args.shift

# Introductory text.
print("\n\t-------------")
print("\tCAESAR CIPHER")
print("\t-------------")
print("\n")

# Set letters in variables [ease of use].
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

# Ask for user input.
plaintext = input("Enter message: ")

def rotate(plaintext, shift):
    
    ciphertext = ""
    for char in plaintext:
    
        if char.isupper():
            # Perform standard monoalphabetic encryption.
            index = ((uppercase.find(char) + shift) % 26)
            ciphertext += (uppercase[index])
    
        elif char.islower():
            index = ((lowercase.find(char) + shift) % 26)
            ciphertext += (lowercase[index])
        
        else:
            # Do not change non-ascii letters.
            ciphertext += (char)

    return ciphertext
        

# Call function, place inside variable.
ciphertext = rotate(plaintext, shift)
print(ciphertext)
