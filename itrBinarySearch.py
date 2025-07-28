#This Program is to perform Binary Search using the Iterative method

def binary_search(l, target):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if l[mid] == target:
            return mid

        elif l[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


list=[]
n=int(input("Enter the Number of items in the list: "))


for i in range(n):
    list.append(int(input("Enter the elements of the list: ")))

target=int(input("Enter the Target Element: "))

list.sort()
result = binary_search(list, target)
print("\n\n",list)
if result != -1:
    print(f"Element {target} is at index {result}. after sorting")
else:
    print(f"Element {target} not found in the list.")
