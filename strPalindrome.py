#This Program is to develop a function to return True if the Inputted String is a Palindrome

def Pal(strrr):
    rev=''
    for i in range(len(strrr) - 1, -1, -1):
        rev= rev + strrr[i]
    if rev==strrr:
        return True
    else:
        return False

str=input("Enter the String: ")
if Pal(str):
    print("Yes, It is a Palindrome")
else:
    print("NO.not a Plaindrome")