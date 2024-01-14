p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e=65537
totient=(p-1)*(q-1)# (f(N)=f(p*q)= totient. if gcd(e,f(N))=1, d=e^-1 mod totient.In the context of RSA, it is typical to choose an encryption exponent e that is coprime with the totient
print(pow(e,-1,totient))
#print(totient)

