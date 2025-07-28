#This Program is to Input a list from the user and check for the Number of Even digits in the list
l=[]
for i in range(5):
    l.append(input("Enter the Elements of the List: "))

count=0
for i in l:
    if i.isdigit():
        if int(i)%2==0:
            count+=1
print(count)