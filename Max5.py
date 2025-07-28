#This Program is to print the Maximum of Five Inputted Numbers and print the maximum number

list=[]

print("Enter 5 Numbers\n")

i=0
while i<5:
    n=int(input("Enter the " + str(i+1) + "th Number: "))
    list.append(n)
    i+=1

largest= list[0]
for max in list:
    if max > largest:
        largest=max

print("The Maximum Number of the Entered Numbers is : "+ str(largest))
