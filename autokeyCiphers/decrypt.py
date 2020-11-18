def decrypt(ciphertext, key):
    key_num = alpha_to_num[key]
    ciphertext_num = []
    for c in ciphertext:
        ciphertext_num.append(alpha_to_num[c])

    plain_num = []
    tmp_key = key_num
    for num in ciphertext_num:
        plain_num.append((num - tmp_key) % 26)
        tmp_key = (num - tmp_key) % 26

    plaintext = []
    for num in plain_num:
        plaintext.append(num_to_alpha[num])

    return ''.join(plaintext)

alpha_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num_to_alpha = {}
alpha_to_num = {}
for i in range(26):
    alpha_to_num[alpha_characters[i]] = i
    num_to_alpha[i] = alpha_characters[i]