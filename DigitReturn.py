#This Program is to Return the Number of digits in a String

str=input("Enter the String to check: ")
digit='1234567890'
def Count(str):
    count = 0
    for itr in str:
        if itr in digit:
            count += 1
    return count

print("The Number of digits in a String is",Count(str))


# count=0
# for itr in str:
#     if itr in digit:
#         count+=1
# print("The Number of digits in a String is",count)

