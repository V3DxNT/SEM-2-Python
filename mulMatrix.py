#This Program is to multiply two matrices using Python Lists

def read_matrix(name, rows, cols):
    print(f"Enter elements for {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
            row.append(val)
        matrix.append(row)
    return matrix

rows1 = int(input("Enter number of rows for Matrix 1: "))
cols1 = int(input("Enter number of columns for Matrix 1: "))

matrix1 = read_matrix("Matrix 1", rows1, cols1)

rows2 = int(input("Enter number of rows for Matrix 2: "))
cols2 = int(input("Enter number of columns for Matrix 2: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible. The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
else:
    # Matrix 2 input
    matrix2 = read_matrix("Matrix 2", rows2, cols2)

    result = []
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            result_row.append(0)
        result.append(result_row)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Resultant Matrix after multiplication:")
    for row in result:
        print(row)
