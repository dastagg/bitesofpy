import secrets
import string


def build_key_part(num_of_chars):
    alphabet = string.ascii_uppercase + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(num_of_chars))
    return password


def gen_key(parts=4, chars_per_part=8):
    license_key = ""
    for x in range(0, parts):
        license_key = license_key + build_key_part(chars_per_part)
        license_key += "-"
    # trim off the last hyphen
    license_key = license_key[:-1]
    return license_key


if __name__ == "__main__":
    print(gen_key())
