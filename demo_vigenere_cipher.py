from vigenereCiphers.encrypt import encrypt
from vigenereCiphers.decrypt import decrypt
from vigenereCiphers.generate_key import generateKey


if __name__ == "__main__": 
    plaintext = "MOINGAYMOTCAUCHUYEN" # Change here
    keyword = "PYTHON" # Change here
    key = generateKey(plaintext, keyword) 
    cipher_text = encrypt(plaintext,key) 
    print("Ciphertext:", cipher_text) 
    print("Plaintext:",  
           decrypt(cipher_text, key))