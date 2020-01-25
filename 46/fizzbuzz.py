def fizzbuzz(num):
    if (int(num) % 3) == 0 and (int(num) % 5) == 0:
        return "FizzBuzz"
    if (int(num) % 3) == 0:
        return "Fizz"
    if (int(num) % 5) == 0:
        return "Buzz"
    return num
