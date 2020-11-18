def encrypt(plaintext, key):
    key_num = alpha_to_num[key]
    plaintext_num = []
    for c in plaintext:
        plaintext_num.append(alpha_to_num[c])
    
    cipher_num = []
    tmp_key = key_num
    for num in plaintext_num:
        cipher_num.append((num + tmp_key) % 26)
        tmp_key = num
    
    ciphertext = []
    for num in cipher_num:
        ciphertext.append(num_to_alpha[num])
    
    return ''.join(ciphertext)

alpha_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num_to_alpha = {}
alpha_to_num = {}
for i in range(26):
    alpha_to_num[alpha_characters[i]] = i
    num_to_alpha[i] = alpha_characters[i]