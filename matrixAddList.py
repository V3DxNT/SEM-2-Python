#This Program is to add two matrices represented by python Lists

def get_matrix_input(rows, cols):
    matrix = []
    print("Enter the elements for a " + str(rows) + "x" + str(cols) + " matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input("Element at position (" + str(i+1) + "," + str(j+1) + "): "))
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition!")
        return

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Main program
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

print("Enter the first matrix:")
matrix1 = get_matrix_input(rows, cols)

print("Enter the second matrix:")
matrix2 = get_matrix_input(rows, cols)

result = add_matrices(matrix1, matrix2)

if result:
    print("Resultant Matrix:")
    for row in result:
        print(row)
