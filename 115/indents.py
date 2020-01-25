def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    space_count = 0

    for letter in text:
        if letter == " ":
            space_count += 1
        else:
            break

    return space_count
