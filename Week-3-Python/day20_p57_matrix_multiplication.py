# ============================================
# Day 20 - Program 57
# Topic: Matrix Multiplication and Shape Rules
# Concepts: (m,n) . (n,p) = (m,p), @ operator,
#           connecting matrix multiply to predictions
# ============================================

import numpy as np


def check_can_multiply(m1: np.ndarray, m2: np.ndarray) -> bool:
    # I check whether two matrices can be multiplied.
    # The inner dimensions must match:
    # (rows1, cols1) and (rows2, cols2) need cols1 == rows2.
    return m1.shape[1] == m2.shape[0]


def multiply_matrices(m1: np.ndarray, m2: np.ndarray) -> np.ndarray:
    # I multiply two matrices using the @ operator.
    return m1 @ m2


def predict_scores(dataset: np.ndarray, weights: np.ndarray) -> np.ndarray:
    # I predict a score for every student in the dataset
    # at once, using one matrix multiplication instead
    # of a loop over each student.
    return dataset @ weights


# --- TESTING ---

A = np.array([[1, 2, 3],
              [4, 5, 6]])           # shape (2, 3)

B = np.array([[1, 0],
              [0, 1],
              [1, 1]])               # shape (3, 2)

print(f"A shape: {A.shape}")
print(f"B shape: {B.shape}")
print(f"Can multiply: {check_can_multiply(A, B)}")

result = multiply_matrices(A, B)
print(f"Result shape: {result.shape}")
print(result)

# I test what happens when shapes do not match.
C = np.array([[1, 2], [3, 4]])       # shape (2, 2)
print(f"Can A multiply with C: {check_can_multiply(A, C)}")

# I apply this to a real student dataset.
student_data = np.array([
    [21, 8.5, 5],
    [20, 9.1, 6],
    [22, 6.5, 3],
])                                    # shape (3, 3)

feature_weights = np.array([0.1, 0.5, 0.4])   # shape (3,)

predictions = predict_scores(student_data, feature_weights)
print(f"Predictions for all students: {predictions}")


