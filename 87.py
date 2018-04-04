a=int(input("first number:"))
b=int(input("second number:"))
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
GCD=gcd(a,b)
print(GCD)
