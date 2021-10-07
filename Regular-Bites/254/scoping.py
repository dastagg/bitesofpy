num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    total = 0
    for num in numbers:
        total += num

    t_hundreds = total // 100
    num_hundreds = num_hundreds + t_hundreds
    return total
