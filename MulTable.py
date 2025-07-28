#This Program is to print a Multplication table of a Number of choice of the User

num= int (input("Enter the Number you want to print the Table of : "))

#USING WHILE LOOP
i=1
while i<=10:
    print(str(num) + ' * ' + str(i) + ' = ' + str(num*i))
    i+=1

print()

#USING FOR LOOP
for j in range(1,11):
    print(str(num) + ' * ' + str(j) + ' = ' + str(num * j))

