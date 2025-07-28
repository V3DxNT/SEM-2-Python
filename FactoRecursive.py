def fact(n):
    if n<=0:
        return 1
    return (n*fact(n-1))

num=int(input("Enter a Number: "))
print("The Factorial of the Number is: " + str(fact(num)))