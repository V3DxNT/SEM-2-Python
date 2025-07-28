#This Program is to Calculate the Mean Variance and Standard Deviation
l=[]
sum=0
n=int(input("Enter the Number: ")) #Length of the list
for i in range(n):
    N=int(input("Enter the Number: "))
    l.append(N)
    sum+=N
mean=sum/n
varSum=0
for i in l:
    varSum+=(i-mean)**2
var=varSum/(n-1)
sd=var**0.5

print("The Mean is :",mean)
print("The Variance is :",var)
print("The Standard Deviation is :",sd)