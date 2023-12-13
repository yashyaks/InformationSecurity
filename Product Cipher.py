''''Product Cipher'''
def rail_fence_encrypt(text, key):
    rail = [["\n" for i in range(len(text))] for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    
    for i in rail:
        print(i)
        
    return "".join(result)

'''Caesar Cipher'''
def caesar_encrypt(plaintext,k):
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

def encrypt_product_cipher(plain_text, caesar_key, rail_fence_key):
    encrypted_text = rail_fence_encrypt(caesar_encrypt(plain_text, caesar_key), rail_fence_key)
    return encrypted_text

plain_text = input("Enter the plain text: ")
caesar_key = int(input("Enter the Caesar key: "))
rail_fence_key = int(input("Enter the Rail Fence key: "))

encrypted_text = encrypt_product_cipher(plain_text, caesar_key, rail_fence_key)
print("Encrypted Text:", encrypted_text)