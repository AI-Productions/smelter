import string


# Replace script w/ the text of what you're scrambling.
script = """We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defense, promote the general"""


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


