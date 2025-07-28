#This Program is to Return the Number of Vowels in a Inputted String

strr=input("Enter the String to check for vowels: ")

counttt=0
vowels="aeiouAEIOU"
for charrr in strr:
    if charrr in vowels:
        counttt+=1

print("The Number of Vowels in the String is :",counttt)

# countt=0
# for chaar in strr:
#     if chaar == 'a' or chaar == 'e' or  chaar == 'i' or chaar == 'o' or  chaar == 'u':
#         countt+=1
#
# print("The Number of Vowels in the String is :",countt)
