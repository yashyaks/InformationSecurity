# p is prime number
# g is primitive root of prime number
# a is private key of Alice
# b is private key of Bob
# Xa is public key of Alice
# Xb is public key of Bob
# Ka is shared key as calculated by alice
# Kb is shared key as calculated by alice

def diffie_hellman(p,g,a,b):
  Xa = pow(g,a)%p 
  Xb = pow(g,b)%p
  Ka = pow(Xb,a)%p
  Kb = pow(Xa,b)%p
  return Xa , Xb , Ka , Kb

Xa , Xb , Ka , Kb = diffie_hellman(23,9,4,3)
print(Xa , Xb , Ka , Kb)

# samw value of Ka and Kb indicate a sucessful key transfer