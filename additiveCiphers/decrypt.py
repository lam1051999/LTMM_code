import helpers.charactermap as charactermap
import sys
sys.path.append("..")


def decrypt(input_str, key):
    input_str = input_str.replace(" ", "")
    input_list = []
    output_list = []
    output_str = ""
    for i in input_str:
        input_list.append(charactermap.CIPHERTEXT_DICT[i])
    for i in input_list:
        if i >= key:
            output_list.append((i - key) % 26)
        else:
            output_list.append((i + 26 - key) % 26)
    character_list = [j for j in charactermap.PLAINTEXT_DICT.keys()]
    for i in output_list:
        output_str += character_list[i]
    return output_str
