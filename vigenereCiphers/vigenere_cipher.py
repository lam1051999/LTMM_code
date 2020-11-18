# Vigenere Cipher 

# Note: Both plaintext and ciphertext are uppercase letters

# This function generates the key in a cyclic manner until  
# its length equal to the length of original text 
def generateKey(plaintext, key): 
    key = list(key) 
    if len(plaintext) == len(key): 
        return(key) 
    else: 
        for i in range(len(plaintext) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the encrypted text generated  
# with the generated key 
def encryption(plaintext, key): 
    cipher_text = [] 
    for i in range(len(plaintext)): 
        x = (ord(plaintext[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
      
# This function decrypts the encrypted text and returns  
# the plaintext
def decryption(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') # 'A' is as the reference alphabet
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
      
# Driver code 
if __name__ == "__main__": 
    plaintext = "MOINGAYMOTCAUCHUYEN"
    keyword = "PYTHON"
    key = generateKey(plaintext, keyword) 
    cipher_text = encryption(plaintext,key) 
    print("Ciphertext:", cipher_text) 
    print("Plaintext:",  
           decryption(cipher_text, key)) 
  