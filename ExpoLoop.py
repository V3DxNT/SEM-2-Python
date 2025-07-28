#This Program is to find the Power of a number N and Print the result

n=int(input("Enter the Number to find the Exponent of: "))
expo=int(input("Enter the Exponent: "))

result = 1

for i in range (expo):
    result*=n

print("The Result of the Exponentiation is: ",result)