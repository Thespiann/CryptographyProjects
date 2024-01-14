p=65537
a=273246787654
#fermats little theorem
#if p=prime, a^p mod p= a
#if a%p!=0 (a not divisble by p), then a^(p-1)-1 = x*p, so a^(p-1)=1 mod p
if a%p !=0:
    print(1)