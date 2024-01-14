from Crypto.PublicKey import RSA
pub = open("bruce_rsa.pub").read()
key = RSA.importKey(pub)
print(key.n)