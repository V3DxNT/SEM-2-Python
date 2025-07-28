#This Program is to add two Sparse Matrix

def read_sparse_matrix(nz, matrix_num):
    print(f"\nEnter elements for Matrix {matrix_num}:")
    sparse = {}
    for i in range(nz):
        print(f"Element {i+1}:")
        row = int(input(" Row: "))
        col = int(input(" Column: "))
        val = int(input(" Value: "))
        sparse[(row, col)] = val
    return sparse

def add_sparse_matrices(mat1, mat2):
    result = {}

    for key in mat1:
        result[key] = mat1[key]

    for key in mat2:
        if key in result:
            result[key] += mat2[key]
            if result[key] == 0:
                del result[key]  # Remove zero to keep sparse
        else:
            result[key] = mat2[key]

    return result

def print_sparse_matrix(sparse_matrix, rows, cols):
    print("\nResultant Matrix:")
    for i in range(rows):
        for j in range(cols):
            print(sparse_matrix.get((i, j), 0), end=' ')
        print()

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

nz1 = int(input("Enter number of non-zero elements in Matrix 1: "))
mat1 = read_sparse_matrix(nz1, 1)

nz2 = int(input("Enter number of non-zero elements in Matrix 2: "))
mat2 = read_sparse_matrix(nz2, 2)

result = add_sparse_matrices(mat1, mat2)
print_sparse_matrix(result, rows, cols)
