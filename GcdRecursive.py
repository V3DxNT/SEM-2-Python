def Gcd(a,b):
    if b==0:
        return a
    return Gcd(b,a%b)

a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("The GCD of the Two Numbers is: " + str(Gcd(a,b)))