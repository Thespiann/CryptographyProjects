from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail.pem', 'r') as key_file:
    key = RSA.importKey(key_file.read())
    private_key_d_decimal = key.d
    print(private_key_d_decimal)