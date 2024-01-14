from pwn import xor
hex='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
bytes=bytes.fromhex(hex)
crypto='crypto{'.encode()
#print(xor(bytes,crypto)) : b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
key='myXORkey'.encode()
print(xor(bytes,key))