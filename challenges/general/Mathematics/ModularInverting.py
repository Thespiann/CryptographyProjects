#For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p
d=0
while (3*d)%13 !=1:
    d=d+1
print(d)