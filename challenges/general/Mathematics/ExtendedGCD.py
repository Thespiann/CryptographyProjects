p = 26513
q = 32321
#p * u + q * v = gcd(p,q)
def egcd(a,b):
    if a==0:
        return b,0,1
    else:
        gcd, u, v= egcd(b%a,a)
        return gcd, v-(b//a)*u, u
gcd,u,v=egcd(p,q)
print(min(u,v))
