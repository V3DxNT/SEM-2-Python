#This Program is to print the N numbers of Fibonacci Sequence

n=int(input("Enter the Number to print the Fibonacci Sequence till: "))

fibo1=0
fibo2=1
fibo3=0
print(fibo1,fibo2,end ="  ")

for i in range(n):
    fibo3 = fibo1 + fibo2
    fibo1= fibo2
    fibo2=fibo3
    print(fibo3,end="  ")

print("\n\n----PRINTED THE FIBONACCI SEQUENCE TILL THE INPUTTED NUMBER ----")