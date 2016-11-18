import string
import colorama
from colorama import Fore, Back, Style

warning = """This script MUST be used with python3 to work properly. Instead of running python word_scrambler.py, run python3 word_scrambler.py"""
print(Fore.RED + warning)
print(Style.RESET_ALL)

script = input("""Please enter the text you would like scrambled:""")

def strip_punctuation(text):
    punctiation_set = set(string.punctuation)
    punctiation_set.add('"')
    punctiation_set.add("'")
    punctiation_set.add('-')
    sanitized_string = ''.join(ch for ch in text if ch not in punctiation_set)

    return sanitized_string.lower()

script = strip_punctuation(script)

script = script.replace("\n", " ").replace("\t", " ")
created_list = script.split(' ')
created_list.sort()
created_set = set(created_list)
created_list = list(created_set)

copy_this = str(created_list).replace("'", '"')

print(copy_this)


