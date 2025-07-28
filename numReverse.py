#This Program is to output the Number obtained after Reversing the Digits of a Number

def Rev(n):
    digit=0
    reve=0
    while(n>0):
        digit=n%10
        n//=10
        reve=reve*10+digit
    return reve


num=int(input("Enter the number: "))
print("The Number obtained after reversing the Number is:",Rev(num))