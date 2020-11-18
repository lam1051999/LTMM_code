from . import is_int
from . import has_invalid_char


def get_input():
    prompt = 0
    input_str = ""
    while(True):
        prompt = input(
            "What do you want to do with additive ciphers? Encrypt(0) or Decrypt(1): ")
        if not is_int.is_int(prompt):
            print("You must input 0 or 1?..........")
        elif int(prompt) != 0 and int(prompt) != 1:
            print("You must input 0 or 1?..........")
        else:
            break

    while(True):
        if int(prompt) == 0:
            input_str = input("Enter the string that you want to encrypt: ")
            input_str = input_str.lower()
        else:
            input_str = input("Enter the string that you want to decrypt: ")
            input_str = input_str.upper()
        if has_invalid_char.has_invalid_char(input_str, int(prompt)):
            print("You must input pure string?..........")
        else:
            break

    return int(prompt), input_str.replace(" ", "")
