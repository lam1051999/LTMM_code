import helpers.charactermap as charactermap
import sys
sys.path.append("..")


def decrypt(input_str):
    input_str = input_str.replace(" ", "")
    output_str = ""
    reversed_dict = {}
    for (key, value) in charactermap.MONOSUB_DICT.items():
        reversed_dict[value] = key
    for i in input_str:
        output_str += reversed_dict[i]
    return output_str
