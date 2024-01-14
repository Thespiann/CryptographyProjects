def gcd(a,b):#function for getting the greatest common divisor
    if a==0:
        return b #if a is 0 then b is the gcd
    else:
        return gcd(b%a,a) #recursion, we call gcd() with the updated values
print(gcd(66528,52920))

