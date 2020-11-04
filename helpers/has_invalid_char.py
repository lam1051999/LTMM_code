from . import charactermap


def has_invalid_char(input_str, prompt):
    input_str = input_str.replace(" ", "")
    char_list = []
    if prompt == 0:
        char_list = [i for i in charactermap.PLAINTEXT_DICT.keys()]
    else:
        char_list = [i for i in charactermap.CIPHERTEXT_DICT.keys()]
    return any(char not in char_list for char in input_str)
