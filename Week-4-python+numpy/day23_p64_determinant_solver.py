# ============================================
# Day 23 - Program 64
# Topic: Determinant and Solving Linear Systems
# Concepts: np.linalg.det, invertibility check,
#           np.linalg.inv, np.linalg.solve
# ============================================

import numpy as np


def calculate_determinant(matrix: np.ndarray) -> float:
    # I calculate the determinant of a square matrix.
    return np.linalg.det(matrix)


def is_invertible(matrix: np.ndarray) -> bool:
    # I check if a matrix can be inverted by testing
    # if its determinant is far enough from zero.
    det = calculate_determinant(matrix)
    return abs(det) > 1e-10


def find_inverse(matrix: np.ndarray) -> np.ndarray:
    # I return the inverse of a matrix, but only
    # after confirming it is invertible.
    if not is_invertible(matrix):
        print("I cannot invert this matrix — determinant is zero.")
        return None
    return np.linalg.inv(matrix)


def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    # I solve Ax = b using NumPy's solve function,
    # which I prefer over manually multiplying by the inverse.
    if not is_invertible(A):
        print("I cannot solve this system — no unique solution.")
        return None
    return np.linalg.solve(A, b)


# --- TESTING ---

A = np.array([[4, 2],
              [3, 5]])

print(calculate_determinant(A))
print(is_invertible(A))

A_inv = find_inverse(A)
print(A_inv)

# I verify that A times its inverse gives the identity matrix.
identity_check = A @ A_inv
print(identity_check)

# I test with a singular matrix (determinant = 0).
singular = np.array([[2, 4],
                      [1, 2]])
print(is_invertible(singular))
print(find_inverse(singular))

# I solve a real system of equations:
# price of pens (x) and notebooks (y)
# 4x + 2y = 18   (bill 1)
# 3x + 5y = 23   (bill 2)
prices_matrix = np.array([[4, 2],
                           [3, 5]])
bills = np.array([18, 23])

solution = solve_linear_system(prices_matrix, bills)
print(f"Pen price: {solution[0]}, Notebook price: {solution[1]}")

