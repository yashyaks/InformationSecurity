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

plaintext = str(input("Input message to be encrypted: "))
key = str(input("Enter the key: "))

cipher_text = vigenere_encrypt(plaintext, key)
print("Cipher Text is: ", cipher_text)