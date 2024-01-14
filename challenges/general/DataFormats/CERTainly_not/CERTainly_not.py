from Crypto.PublicKey import RSA
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open('2048b-rsa-example-cert.der', 'rb') as der_file:
    cert = x509.load_der_x509_certificate(der_file.read(), default_backend())

with open('2048b-rsa-example-cert.pem', 'wb') as pem_file:
    pem_file.write(cert.public_bytes(encoding=serialization.Encoding.PEM))
with open('2048b-rsa-example-cert.pem', 'r') as key_file:
    key = RSA.import_key(key_file.read())
    print(type(key))
    print(key.n)