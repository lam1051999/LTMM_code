import helpers.charactermap as charactermap
import sys
sys.path.append("..")


def encrypt(input_str):
    input_str = input_str.replace(" ", "")
    output_str = ""
    for i in input_str:
        output_str += charactermap.MONOSUB_DICT[i]
    return output_str
