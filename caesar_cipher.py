'''Caesar Cipher'''
def encrypt_text(plaintext,k):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + k-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + k-97) % 26 + 97)
    return ans

def decrypt_text(ciphertext, k):
    ans = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - k-65) % 26 + 65)
        else:
            ans += chr((ord(ch) - k-97) % 26 + 97)
    return ans

#Inputs
plaintext = str(input("Input message to be encrypted: "))
k = int(input("Key value: "))

#Encryption
encrypted_text = encrypt_text(plaintext,k)
print("Cipher Text is : ",encrypted_text)

#Decryption
decrypted_text = decrypt_text(encrypted_text, k)
print("Decrypted Text is: ", decrypted_text)