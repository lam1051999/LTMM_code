import autokeyCiphers.encrypt as encrypt
import autokeyCiphers.decrypt as decrypt
import helpers.get_input as get_input

prompt, input_str = get_input.get_input()
key = 'N'  # change this parameter

if prompt == 0:
    print("Encrypted string (cipher text) (with key=" +
          str(key) + "): ", encrypt.encrypt(input_str, key))
else:
    print("Decrypted string (plain text) (with key=" +
          str(key) + "): ", decrypt.decrypt(input_str, key))
