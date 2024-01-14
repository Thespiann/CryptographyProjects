p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N=p*q
#Euler’s totient function is a multiplicative function, meaning that if two numbers and are relatively prime, then, φ(p*q)=φ(p)*φ(q). If p is a prime, then f(p)=p-1, because all the numbers up to p are not divisible by p
totient=(p-1)*(q-1)
print(totient)