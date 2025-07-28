#This Program is to perform Linear Search using the Recursive Method

def LinearSearch(list,key,index=0):
    if index<len(list):
        if list[index]==key:
            print("The Key is at Index: ", index)
        else:
            LinearSearch(list,key,index+1)
    else:
        print("The Key is Not Found: ")

#input the list
l=[1,35,54,241,423,532]
key=int(input("Enter the Key to Search: "))
LinearSearch(l,key)