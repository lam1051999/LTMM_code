import helpers.inv_number_modulo as inv_number_modulo
import helpers.charactermap as charactermap
import sys
sys.path.append("..")


def decrypt(input_str, key):
    input_str = input_str.replace(" ", "")
    input_list = []
    output_list = []
    output_str = ""
    key_0 = inv_number_modulo.inv_number_modulo(key[0], 26)
    for i in input_str:
        input_list.append(charactermap.CIPHERTEXT_DICT[i])
    output_list = [(((i - key[1]) * key_0) % 26) for i in input_list]
    character_list = [i for i in charactermap.PLAINTEXT_DICT.keys()]
    for i in output_list:
        output_str += character_list[i]
    return output_str
