from autokeyCiphers.encrypt import encrypt
from autokeyCiphers.decrypt import decrypt


print('Enter an example plaintext: ', end='')
plaintext = str(input()).upper()
key = 'N' # change this parameter

ciphertext = encrypt(plaintext, key)
print('Ciphertext:', ciphertext)

plaintext = decrypt(ciphertext, key)
print('Plaintext:', plaintext)