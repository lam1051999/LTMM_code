# This function decrypts the encrypted text and returns  
# the plaintext
def decrypt(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') # 'A' is as the reference alphabet
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 