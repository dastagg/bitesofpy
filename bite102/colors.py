VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    while True:
        choice = input("Enter your favorite color: ")
        if choice.lower() == 'quit':
            print("bye")
            break
        elif choice.lower() not in VALID_COLORS:
            print("Not a valid color")
            continue
        else:
            print(choice.lower())
            continue
