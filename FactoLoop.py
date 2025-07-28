#this Program is to Find the Factorial of a Number using Loop

num=int(input("Please Enter the Number for Factorial: "))

fact=1
for i in range(1,num+1):
    fact*=i

print("The factorial of the Number is : ",fact)