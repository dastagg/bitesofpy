import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    new_string = ""

    for letter in input_string:
        if letter in string.punctuation:
            continue
        else:
            new_string += letter

    return new_string
