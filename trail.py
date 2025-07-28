# # m1=int(input("Enter the Marks of the First Subject: "))
# # m2=int(input("Enter the Marks of the Second Subject: "))
# # m3=int(input("Enter the Marks of the Third Subject: "))
# #
# # m=[m1,m2,m3]
# #
# # i=0
# # c=0
# # while i<len(m):
# #     if m[i]<40:
# #         c+=1
# #     i+=1
# #
# # if c<=1:
# #     print("The Student failed in: " + str(c) + " Subject")
# # else:
# #     print("The Student failed in: " + str(c) + " Subjects")
#
# def GASEq(): #pv=nrt
#     p=int(input("Enter the pressure"))
#     r= int(input("Enter the gas value constant"))
#     n = int(input("Enter the number of moles of gas present"))
#     t = int(input("Enter the temperature at which the process is being taking place"))
#     v=(n*r*t)/p
#     print("The volume of the gas is :" + str(v))
# a= True
# while (a==True):
#     #print("Hi do you want to further print, 1 for YES and 0 for NO : ")
#     choice= input("Please Enter your CHOICE for the Program: ")
#     if choice.casefold("Gas EQUATIOn"):
#         GASEq()
#
#     x=int(input("Hi do you want to further print, 1 for YES and 0 for NO : "))
#     if x==1:
#         a=True
#     elif x==0:
#         a=False
#
#
# z=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(z):
#     print(str(z[i]) + 'hi ' + str(i)+ 'hello', end="")
#     i+=1
# print("\nDone")
#

# s1=int(input("Enter the First Side of the Triangle: "))
# s2=int(input("Enter the Second Side of the Triangle: "))
# s3=int(input("Enter the Third Side of the Triangle: "))
#
# if s1>0 and s2>0 and s3>0:
#     if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
#         if s1==s2 and s2==s3:
#             print("Equilateral Triangle")
#         elif s1==s2 or s1==s3:
#             print("Isoscles Triangle")
#         else:
#             print("Scalene Triangle")
#
#     else:
#         print("Not A Valid Triangle")
#
# else:
#     print("All sides of a triangle should be positive")

# list=[]
# for i in range(5):
#     n=int(input("Enter the Number: "))
#     list.append(n)
#
# print(list)
# max=list[0]
# for num in list:
#     if num>max:
#         max=num
# print("The Maximum Element in the List is: ",max)
#
# list=[]
# for i in range(5):
#     n=input("Enter the String: ")
#     list.append(n)
# target=input("Enter the word you want to search for: ")
# print(list)
# for charr in list:
#     if charr== target:
#         print("The Element found : ")
#         break
flag=True
while flag:
    print("VEDANT")
    print("DO you want to continue printing (Y/N) : ",end=" ")
    choice=input()
    if choice.lower() == 'n':
        print("\n\n\n\n\nThank You")
        flag=False

































