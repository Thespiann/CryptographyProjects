xor= [chr(ord(char)^13) for char in "label"]
new=''.join(xor)
print("crypto{"+new+"}")