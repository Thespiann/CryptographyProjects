p= 991
g=209
# g*d mod p =1
for x in range(p):
    res= (g*x)%p
    if res==1:
        print(x)
        break