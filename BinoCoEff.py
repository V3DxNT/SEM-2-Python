#this program is to Print the Binomial CoEffecient of the Inputed Number

def facttt(num):
    if num<=1:
        return 1
    return num * facttt(num - 1)

n = int (input("Enter the N of the CoEffecient: "))
k = int (input("Enter the K of the CoEffecient: "))

C = (facttt(n)) / (facttt(k) * facttt(n-k))

print("The Binomial CoEffecient of the Number is:"+ str(C))