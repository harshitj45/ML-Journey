matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Task 1: Flatten
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
print("Flat:", flat)

# Task 2: Transpose
rows = len(matrix)
cols = len(matrix[0])

transposed = []
for c in range(cols):
    new_row = []
    for r in range(rows):
        new_row.append(matrix[r][c])
    transposed.append(new_row)

print("Transposed:")
for row in transposed:
    print(row)

# Task 3: Elements > 5
greater_than_5 = []
for row in matrix:
    for x in row:
        if x > 5:
            greater_than_5.append(x)
print("Elements > 5:", greater_than_5)

# Task 4: Square each element
squared = []
for row in matrix:
    new_row = []
    for x in row:
        new_row.append(x**2)
    squared.append(new_row)

print("Squared:")
for row in squared:
    print(row)

# Task 5: Sum of each row
row_sums = []
for row in matrix:
    total = 0
    for x in row:
        total += x
    row_sums.append(total)
print("Row sums:", row_sums)

# Task 6: Sum of each column
col_sums = []
for c in range(cols):
    total = 0
    for r in range(rows):
        total += matrix[r][c]
    col_sums.append(total)
print("Col sums:", col_sums)

# Task 7: Diagonal elements
diagonal = []
for i in range(rows):
    diagonal.append(matrix[i][i])
print("Diagonal:", diagonal)

# Task 8: Normalize each row
row_normalized = []
for row in matrix:
    total = sum(row)
    new_row = []
    for x in row:
        new_row.append(x / total)
    row_normalized.append(new_row)

print("Row normalized:")
for row in row_normalized:
    print(row)

# Task 9: Matrix multiplication
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

result = []

for i in range(len(A)):
    new_row = []
    for j in range(len(B[0])):
        total = 0
        for k in range(len(B)):
            total += A[i][k] * B[k][j]
        new_row.append(total)
    result.append(new_row)

print("Matrix multiply result:")
for row in result:
    print(row)