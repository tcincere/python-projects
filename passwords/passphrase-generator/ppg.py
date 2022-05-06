

from random import randint
import argparse

    
parser = argparse.ArgumentParser (
        
    description="Pass-phrase generator using english wordlist.\n\twritten by tcincere", 
    epilog="github: https://github.com/tcincere"
    
)

delimiter_set = ['[', ']', '{', '}', '-', '/', ',', '.', ':']
case_dictionary = {"u": "Upper-case", "l": "Lower-case", "t": "Title-case"}     
    
parser.add_argument (
        
    "-d", "--delimiter",
    metavar="delimiter",
    type=str,
    choices=delimiter_set,
    help="Add a delimiter between words e.g. - or : etc",
    default=delimiter_set[4],
    dest="delimiter"

)

parser.add_argument (
        
    "-c",
    metavar="case",
    type=str,
    choices=case_dictionary.keys(),
    help="Case for the pass-phrase e.g. (u)pper, (l)ower, (t)itle",
    default='t',
    dest="case"

)

parser.add_argument (
        
    "-n",
    metavar="number of words",
    type=int,
    choices=range(1, 51),
    help="Number of words within pass-phrase e.g. min = 1, max = 50",
    default=6,
    dest="number_of_words"
    
    
)

args = parser.parse_args()

delimiter = args.delimiter
case = args.case
number_of_words = args.number_of_words

def procure_word(number_of_words):

    try: 
        file = open("words_alpha.txt", "r")
    except FileNotFoundError as e:
        print(e)

    line = file.readlines()
    line_length = len(line) - 1
    
    words_list = []
    
    i = 0
    while i < number_of_words: 
               
        random_number = randint(0, line_length)
        words_list.append(line[random_number].strip())
        i += 1
        
    file.close()
    return words_list


def manipulate(case, delimiter, words_list):
   
    words_list = delimiter.join(words_list)
    
    string = ""

    if case == 'u':
        string = words_list.upper()
        
    elif case == 'l':
        string = words_list.lower()
         
    elif case == 't':
       string = str.title(words_list)
        
    return string



words_list = procure_word(number_of_words)
passphrase = manipulate(case, delimiter, words_list)

print(passphrase)