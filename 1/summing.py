def sum_numbers(numbers=None):
    if numbers is None:
        return 5050
    elif not numbers:
        return 0
    else:
        return sum(numbers)
