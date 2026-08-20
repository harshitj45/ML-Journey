# ============================================
# Day 23 - Program 65
# Topic: Eigenvalues and Eigenvectors
# Concepts: np.linalg.eig, Av = lambda*v,
#           np.allclose for verification
# ============================================

import numpy as np


def get_eigen_pairs(matrix: np.ndarray) -> tuple:
    # I calculate the eigenvalues and eigenvectors
    # of a square matrix.
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def verify_eigenpair(matrix: np.ndarray, vector: np.ndarray, value: float) -> bool:
    # I confirm that A @ v equals lambda * v for this pair.
    # I use allclose instead of == because of floating point rounding.
    left_side = matrix @ vector
    right_side = value * vector
    return np.allclose(left_side, right_side)


def verify_all_eigenpairs(matrix: np.ndarray) -> list:
    # I verify every eigenvalue-eigenvector pair for a matrix
    # and return a list of True/False results.
    eigenvalues, eigenvectors = get_eigen_pairs(matrix)
    results = []
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lam = eigenvalues[i]
        is_valid = verify_eigenpair(matrix, v, lam)
        results.append(is_valid)
    return results


def largest_eigenvalue(matrix: np.ndarray) -> float:
    # I find the largest eigenvalue, which later becomes
    # important for understanding which direction in the
    # data carries the most variation.
    eigenvalues, _ = get_eigen_pairs(matrix)
    return max(eigenvalues)


# --- TESTING ---

A = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = get_eigen_pairs(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

results = verify_all_eigenpairs(A)
print(f"Verification results: {results}")

biggest = largest_eigenvalue(A)
print(f"Largest eigenvalue: {biggest}")

# I test with a different matrix.
B = np.array([[2, 0],
              [0, 5]])
print(get_eigen_pairs(B))
print(verify_all_eigenpairs(B))

