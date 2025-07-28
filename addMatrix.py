#This is a program to add two matrices represented using Python Lists

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

def matrix(name):
    print(f"Enter elements for {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
            row.append(val)
        matrix.append(row)
    return matrix

matrix1 = matrix("Matrix 1")
matrix2 = matrix("Matrix 2")

result = []
for i in range(rows):
    rrow = []
    for j in range(cols):
        rrow.append(matrix1[i][j] + matrix2[i][j])
    result.append(rrow)

print("Resultant Matrix:")
for row in result:
    print(row)
