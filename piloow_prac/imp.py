# import json
from string import ascii_uppercase, ascii_lowercase, digits
# dicta = {
#     "athrva":"shitole",
#     "ram":"laxman",
#     "dev":"mann"
# }

def contains(required_chars, s):
    return any(c in required_chars for c in s)

def contains_upper(s):
    return contains(ascii_uppercase, s)

def contains_lower(s):
    return contains(ascii_lowercase, s)

def contains_digit(s):
    return contains(digits, s)

def contains_special(s):
    return contains(r"""!@$%^&*()_-+={}[]|\,.></?~`"':;""", s)

def long_enough(s):
    return len(s) >= 8

def validate_password(password):
    VALIDATIONS = (
        (contains_upper, 'Password needs at least one upper-case character.'),
        (contains_lower, 'Password needs at least one lower-case character.'),
        (contains_digit, 'Password needs at least one number.'),
        (contains_special, 'Password needs at least one special character.'),
        (long_enough, 'Password needs to be at least 8 characters in length.'),
    )
    failures = [
        msg for validator, msg in VALIDATIONS if not validator(password)
    ]
    if not failures:
        return True
    else:
        print("Invalid password! Review below and change your password accordingly!\n")
        for msg in failures:
            print(msg)
        print('')
        return False

pasw = input("password: ")
if (validate_password(pasw)):
    print("okk")
#     print(i, " : ", dicta[i])