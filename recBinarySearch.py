#sevenA
#This program is to perform a Recursive Binary Search on a sorted list of names. The function returns the index of the
#name passed as an argument to function

def recursive_binary_search(names, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if names[mid] == target:
        return mid
    elif names[mid] > target:
        return recursive_binary_search(names, target, low, mid - 1)
    else:
        return recursive_binary_search(names, target, mid + 1, high)

names = []
n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input("Enter name {}: ")
    names.append(name)

names.sort()
target = input("Enter the name to search for: ")

index = recursive_binary_search(names, target, 0, len(names) - 1)

if index != -1:
    print(target, "found at index", index)
else:
    print(target, "not found in the list")
