import helpers.charactermap as charactermap
import sys
sys.path.append("..")


def encrypt(input_str, key):
    input_str = input_str.replace(" ", "")
    input_list = []
    output_str = ""
    for i in input_str:
        input_list.append(charactermap.PLAINTEXT_DICT[i])
    output_list = [((i * key[0] + key[1]) % 26) for i in input_list]
    character_list = [i for i in charactermap.CIPHERTEXT_DICT.keys()]
    for i in output_list:
        output_str += character_list[i]
    return output_str
