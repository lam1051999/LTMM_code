# This function returns the encrypted text generated
# with the generated key
def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    cipher_text = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
