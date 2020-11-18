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