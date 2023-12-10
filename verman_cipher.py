'''Verman Cipher'''

def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

plaintext = str(input("Input message to be encrypted: "))
key = str(input("Enter the key: "))

cipher_text = vigenere_encrypt(plaintext, key)
print("Cipher Text is: ", cipher_text)

decrypted_text = vigenere_decrypt(cipher_text, key)
print("Decrypted Text is: ", decrypted_text)
