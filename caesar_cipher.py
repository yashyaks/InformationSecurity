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

#Inputs
plaintext = str(input("Input message to be encrypted: "))
k = int(input("Key value: "))

#Encryption
encrypted_text = encrypt_text(plaintext,k)
print("Cipher Text is : ",encrypted_text)

#Brute force
def bruteforce_caesar(ciphertext):
    print(ciphertext)
    for i in range(1,27):
        decipher_text = ""
        k = i
        for i in range(len(ciphertext)):
            ch = ciphertext[i]
            if ch == " ":
                decipher_text += " "
            elif ch.isupper():
                decipher_text += chr((ord(ch) - k-65) % 26 + 65)
            else:
                decipher_text += chr((ord(ch) - k-97) % 26 + 97)

        print (decipher_text ,k)

bruteforce_caesar(encrypted_text)