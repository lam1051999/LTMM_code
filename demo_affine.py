import affineCiphers.decrypt as decrypt
import affineCiphers.encrypt as encrypt
import helpers.get_input as get_input

prompt, input_str = get_input.get_input()
key = (7, 2)
if prompt == 0:
    print("Encrypted string: ", encrypt.encrypt(input_str, key))
else:
    print("Decrypted string: ", decrypt.decrypt(input_str, key))
