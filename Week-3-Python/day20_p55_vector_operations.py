# ============================================
# Day 20 - Program 55
# Topic: Vector Operations with NumPy
# Concepts: vector add/subtract, scalar multiply,
#           dot product, L2 norm, distance
# ============================================

import numpy as np


def add_vectors(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    # I add two vectors element by element.
    return v1 + v2


def scale_vector(v: np.ndarray, scalar: float) -> np.ndarray:
    # I multiply every element of the vector by a scalar.
    return v * scalar


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    # I calculate the dot product of two vectors.
    return np.dot(v1, v2)


def vector_length(v: np.ndarray) -> float:
    # I calculate the L2 norm, which is the vector's length.
    return np.linalg.norm(v)


def euclidean_distance(p1: np.ndarray, p2: np.ndarray) -> float:
    # I calculate the distance between two points
    # by finding the norm of their difference.
    return np.linalg.norm(p2 - p1)


def weighted_score(features: np.ndarray, weights: np.ndarray) -> float:
    # I combine features and weights using a dot product.
    # This is the same calculation a linear model uses
    # to turn features into a single prediction.
    return np.dot(features, weights)


# --- TESTING ---

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(add_vectors(v1, v2))          # [5 7 9]
print(scale_vector(v1, 3))          # [3 6 9]
print(dot_product(v1, v2))          # 32

print(vector_length(np.array([3, 4])))   # 5.0

p1 = np.array([0, 0])
p2 = np.array([3, 4])
print(euclidean_distance(p1, p2))   # 5.0

student_features = np.array([21, 8.5, 5])
feature_weights = np.array([0.1, 0.5, 0.4])
print(weighted_score(student_features, feature_weights))


