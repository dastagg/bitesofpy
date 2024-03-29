"""Find the 'wrong char' in a series of chars."""

# This is one version from the net.
# def get_index_different_char(chars):
#     alpha, non_alpha = set(), set()
#     for i, char in enumerate(chars):
#         if str.isalnum(str(char)):
#             alpha.add(i)
#         else:
#             non_alpha.add(i)
#     return next(iter(alpha)) if len(alpha) == 1 else next(iter(non_alpha))



import string

letters = string.ascii_letters
numbers = string.digits
alphanums = letters + numbers


def get_index_different_char(chars):
    num_alphas = 0
    num_non_alphas = 0

    for i in range(len(chars)):
        if str(chars[i]) == "":
            num_non_alphas += 1
        elif str(chars[i]) not in alphanums:
            num_non_alphas += 1
        else:
            num_alphas += 1

    for i in range(len(chars)):
        if num_alphas > 1 and str(chars[i]) not in alphanums:
            return i
        elif num_non_alphas > 1 and str(chars[i]) != "" and str(chars[i]) in alphanums:
            return i


def main():
    test1 = ["A", "f", ".", "Q", 2]
    print("Test 1: ")
    print(get_index_different_char(test1))
    test2 = [".", "{", " ^", "%", "a"]
    print("Test 2 ")
    print(get_index_different_char(test2))


if __name__ == "__main__":
    main()
