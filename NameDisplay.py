#This Program is to input 5 Names from the User and Check whether the target name is present or not

list=[]

for i in range(5):
    n=input("Enter the NAME of the " + str(i+1) + "th Student: ")
    list.append(n)

target =input("\nEnter the Name that you want to Check: ")

flag=0
for choice in list:
    if choice == target:
        flag=1
    #else:
        #flag=0

if flag==1:
    print("\n--The Name is FOUND--")

else:
    print("---The name is NOT FOUND---")