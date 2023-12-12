# Man in the Middle attack on DiffieHellman Key Exchange Algorithm

def deffie(a,b,g,p):
  Xa=pow(g,a,p)
  Xb=pow(g,b,p)
  return Xa, Xb

# prime number and primitive root
p=23
g=9
# private keys of Alice and Bob respectively
priv_a = 5
priv_b = 6
# two random private keys as calculated by Darth
priv_c=11
priv_d=13

# Alice and Bob trying to exchange keys as per usual according to diffieHellman
# Xa is public key of Alice
# Xb is public key of Bob
Xa,Xb=deffie(priv_a,priv_b,g,p)
print(f"Alice sends her public key(Xa), {Xa} to Bob")
print(f"Bob sends his public key(Xb), {Xb} to Alice")

# but, Darth intercepts the public keys of alice and bob
# darth calculates public keys to share with both alice and bob
# Xc is the public key to be shared with Bob, allegedly originating from Alice
# Xd is the public key to be shared with Alice, allegedly originating from Bob

Xc,Xd=deffie(priv_c,priv_d,g,p)
print("Darth intercepts public key of Alice Xa, being sent to Bob" +
      f"and instead sends Xc (a darth-bob public key) {Xc}, to Bob")
print("Darth intercepts public key of Bob Xb, being sent to Alice" +
      f"and instead sends Xd (a darth-alice public key) {Xc}, to Alice")

# Now ALice had a public key from Darth and Darth has a public key from Alice, opening up a communication channel btwn them
# Also Bob had a public key from Darth and Darth has a public key from Bob, opening up a communication channel btwn them


# Dka being a shared key for Alice as calculated by Darth
DKa=pow(Xa,priv_d,p)
print("Darth calculates shared key of ALice as ",DKa)
# Ka being a shared key as calculated by Alice
Ka=pow(Xc,priv_a,p)
print("Alice calculates shared key unaware of the attack as ",Ka)

# When DKa and Ka match, it will indicate a successful key exchange for Alice but in reality a MITM attack has been executed


# Dkb being a shared key for Bob as calculated by Darth
DKb=pow(Xb,priv_c,p)
print("Darth calculates secret key of Bob as ",DKb)
# Kb being a shared key as calculated by Bob
Kb=pow(Xd,priv_b,p)
print("Bob calculates secret key unaware of the attack as ",Kb)

# When DKb and Kb match, it will indicate a successful key exchange for Bob but in reality a MITM attack has been executed