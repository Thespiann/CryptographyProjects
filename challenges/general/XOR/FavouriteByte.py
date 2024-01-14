from pwn import xor
hex='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytes=bytes.fromhex(hex)
for i in range(255):
    flag= xor(bytes,i)
    if flag.startswith(b'crypto'):
        print(xor(bytes,i))
        print("secret key is: " + str(i))
        break