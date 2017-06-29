import re

def reg(email):
    """verify that email field, if optionally used, has chars@chars.chars."""
    try:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            if email != '':
                return True
    except ValueError:
        return False

def no_field_blank(username, password, verify):
    """All fields must have content."""
    try:
        if (username == '') or (password == '') or (verify == ''):
            return True
    except ValueError:
        return False

def usersname_length(username):
    """Username must be between 3 and 20 characters"""
    try:
        username = str(username)
        # if username.length() > 3 and < 21:
        if (len(username) >= 3) and (len(username) < 21):
            return True
    except ValueError:
        return False

def do_passwords_match(password, verify):
    """Passwords must match"""
    try:
        if password == verify:
            return True
    except ValueError:
        return False

def passwords_length(password):
    """Passwords must be at least 8 characters"""
    try:
        if len(password) > 7:
            return True
    except ValueError:
        return False

def do_passwords_and_username_match(username, password):
    """Passwords cannot match username"""
    try:
        if password == username:
            return True
    except ValueError:
        return False

def is_integer(num):
    """post."""
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_string(num):
    """post."""
    try:
        str(num)
        return True
    except ValueError:
        return False


# encryption section
def alphabet_position(character):
    """Find alapbetical position of current character."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):
    """Rotate string using magical number 13."""
    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]
    return rotated

def rotate_character(char, rot):
    """Rotate char forward by rot chars."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26
    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(text, rot):
    """Rotate text string forward by rot chars."""
    rotated = ''
    for char in text:
        if char.isalpha():
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char
    return rotated

def basic_external_method_example(text):
    return text
