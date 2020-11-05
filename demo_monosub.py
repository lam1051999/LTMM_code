import monosubCiphers.encrypt as encrypt
import monosubCiphers.decrypt as decrypt
import helpers.get_input as get_input

prompt, input_str = get_input.get_input()
if prompt == 0:
    print("Encrypted string: ", encrypt.encrypt(input_str))
else:
    print("Decrypted string: ", decrypt.decrypt(input_str))
