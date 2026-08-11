# ============================================
# Day 20 - Program 56
# Topic: Matrix Creation and Basic Operations
# Concepts: 2D arrays, shape, indexing,
#           addition, transpose
# ============================================

import numpy as np


def build_dataset(rows: list) -> np.ndarray:
    # I convert a list of student records into a matrix.
    return np.array(rows)


def get_shape_info(matrix: np.ndarray) -> dict:
    # I extract useful shape information from a matrix.
    rows, cols = matrix.shape
    return {"rows": rows, "columns": cols}


def get_feature_column(matrix: np.ndarray, col_index: int) -> np.ndarray:
    # I extract a single column, which represents
    # one feature across all data points.
    return matrix[:, col_index]


def get_student_row(matrix: np.ndarray, row_index: int) -> np.ndarray:
    # I extract a single row, which represents
    # one student's full set of features.
    return matrix[row_index]


def add_matrices(m1: np.ndarray, m2: np.ndarray) -> np.ndarray:
    # I add two matrices together, element by element.
    return m1 + m2


def transpose_matrix(matrix: np.ndarray) -> np.ndarray:
    # I flip rows into columns and columns into rows.
    return matrix.T


# --- TESTING ---

student_data = build_dataset([
    [21, 8.5, 5],
    [20, 9.1, 6],
    [22, 6.5, 3],
])

info = get_shape_info(student_data)
print(f"I have {info['rows']} students and {info['columns']} features")

cgpa_column = get_feature_column(student_data, 1)
print(f"All CGPA values: {cgpa_column}")

first_student = get_student_row(student_data, 0)
print(f"First student's features: {first_student}")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(add_matrices(A, B))

print(f"Original shape: {student_data.shape}")
transposed = transpose_matrix(student_data)
print(f"Transposed shape: {transposed.shape}")

