def Fibo(n):
    if n==0 or n==1:
        return n
    return Fibo(n-1) + Fibo(n-2)

num= int(input("Enter the Number to find FIBONACCI of: "))
for i in range(0,10):
    print("Fibo is: " + str(Fibo(i)))
print("The FIBONACCI of the Number is: " + str(Fibo(num)))