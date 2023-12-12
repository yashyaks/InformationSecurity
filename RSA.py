import math

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

p = 13
q = 17
n = p * q
e = 2
phi = (p - 1) * (q - 1)

while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

d = pow(e, -1, phi)
msg = 96 
print("Message data =", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n)
print("Encrypted data =", c)

# Decryption m = (c ^ d) % n
m = pow(c, d, n)
print("Original Message Sent =", m)