#Program to read USN, Name and Marks in Three Subjects and print all details along with Total and Percentage and count number of Subjects passed

USN=input("Please Enter the USN of the Student: ")
Name_=input("Please Enter the Name  of the Student: ")
m1=int(input("Enter the Marks in First Subject: "))
m2=int(input("Enter the Marks in Second Subject: "))
m3=int(input("Enter the Marks in Third Subject: "))

total_= (m1+m2+m3)
percentage_ = (total_ / 300) * 100

print()
print("The USN of the Student is: " + USN)
print("The Name  of the Student is: " + Name_)
print("The Total Marks in Three Subjects is: " + str(total_))
print("The Percentage of the Student is: " + str(percentage_))

#___________________________________________________________________________
c=0
if m1>40:
    c+=1

if m2>40:
    c+=1

if m3>40:
    c+=1
print("Number of Subjects Passed is: " + str(c))
#___________________________________________________________________________
# m=[m1,m2,m3]
# i=0
# c=0
# while i<len(m):
#     if m[i]<40:
#         c+=1
#     i+=1
# print("The Student failed in: " + str(c))
#___________________________________________________________________________
#
# if(m1>40 and m2>40 and m3>40):
#     print("---Student Passed in ALL SUBJECTS---")
#
# elif ((m1>40 and m2>40) or (m2>40 and m3>40) or (m1>40 and m3>40)):
#     print("---Student Passed in TWO SUBJECTS---")
#
# elif ((m1>40 and m2<40 and m3<40) or (m2>40 and m1<40 and m3<40) or (m3>40 and m1<40 and m2<40)):
#     print("---Student has Passed only in ONE SUBJECT---")
#
# else:
#     print("---Student has passed in NO SUBJECTS---")

print()

