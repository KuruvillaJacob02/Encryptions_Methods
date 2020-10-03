# Transposition Cipher is a cryptographic algorithm where the order of alphabets in the plaintext is rearranged to form a cipher text.

def transpositionCipher(key, message):   
    
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
            
    return ''.join(ciphertext) #Cipher text
