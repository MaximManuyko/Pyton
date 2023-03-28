def invert_case(s):
    """
    Принимает на вход строку s и меняет регистр каждой буквы на противоположный.
    """
    inverted_s = ""
    for char in s:
        if char.islower():
            inverted_s += char.upper()
        elif char.isupper():
            inverted_s += char.lower()
        else:
            inverted_s += char
    return inverted_s
