import vigenereCiphers.decrypt as decrypt
import vigenereCiphers.encrypt as encrypt
import helpers.get_input as get_input
import vigenereCiphers.generate_key as generate_key

prompt, input_str = get_input.get_input()
keyword = "PYTHON"
key = generate_key.generateKey(input_str, keyword)

if prompt == 0:
    print("Encrypted string (cipher text) (with key=" +
          str(key) + "): ", encrypt.encrypt(input_str, key))
else:
    print("Decrypted string (plain text) (with key=" +
          str(key) + "): ", decrypt.decrypt(input_str, key))
