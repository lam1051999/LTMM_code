from helpers import encrypt
from helpers import decrypt

encrypt_input = "we are one xyz"
decrypt_input = "LTPGTDCTMNO"
print(encrypt.encrypt(encrypt_input, 15))
print(decrypt.decrypt(decrypt_input, 15))
