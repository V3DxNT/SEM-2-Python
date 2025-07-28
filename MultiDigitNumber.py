#This Program is to input a MultiDigitNumber and develop a program that prints the frequency of each digit  with Suitable messages

n=input("Input a multi Digit Number: ")
d={}
for i in n:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in sorted(d):
    print(i,"Occured",d[i],"Times")
