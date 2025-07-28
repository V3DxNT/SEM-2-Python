# This Program is to Create a list, Input the Numbers and print the Mean, Variance, and Standard Deviation

numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = float(input("Enter number: "))
    numbers.append(num)

total = 0
for num in numbers:
    total = total + num
mean = total / n

var_sum = 0
for num in numbers:
    var_sum = var_sum + (num - mean) ** 2
variance = var_sum / n

deviation = variance ** 0.5

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", deviation)
