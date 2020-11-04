import additiveCiphers.encrypt as encrypt
import additiveCiphers.decrypt as decrypt
import helpers.get_input as get_input

prompt, input_str = get_input.get_input()
key = 15
if prompt == 0:
    print("Encrypted string: ", encrypt.encrypt(input_str, key))
else:
    print("Decrypted string: ", decrypt.decrypt(input_str, key))
