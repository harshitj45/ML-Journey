# ============================================
# Day 22 - Program 61
# Topic: L1 Norm, L2 Norm, Unit Vectors
# Concepts: Manhattan distance, Euclidean distance,
#           vector normalization
# ============================================

import numpy as np


def manhattan_distance(p1: np.ndarray, p2: np.ndarray) -> float:
    # I calculate the L1 distance by summing the
    # absolute differences between the two points.
    return np.sum(np.abs(p2 - p1))


def euclidean_distance(p1: np.ndarray, p2: np.ndarray) -> float:
    # I calculate the L2 distance using the norm
    # of the difference between the two points.
    return np.linalg.norm(p2 - p1)


def compare_distances(p1: np.ndarray, p2: np.ndarray) -> dict:
    # I return both distance measures together
    # so I can compare how they differ.
    return {
        "manhattan": manhattan_distance(p1, p2),
        "euclidean": euclidean_distance(p1, p2),
    }


def normalize(vector: np.ndarray) -> np.ndarray:
    # I convert any vector into a unit vector.
    # I keep the direction but make the length exactly 1.
    magnitude = np.linalg.norm(vector)
    if magnitude == 0:
        return vector
    return vector / magnitude


def is_unit_vector(vector: np.ndarray) -> bool:
    # I check whether a vector already has length 1.
    return np.isclose(np.linalg.norm(vector), 1.0)


# --- TESTING ---

point_a = np.array([1, 1])
point_b = np.array([4, 5])

result = compare_distances(point_a, point_b)
print(result)

v = np.array([3, 4])
unit_v = normalize(v)
print(f"Original vector: {v}")
print(f"Unit vector: {unit_v}")
print(f"Length of unit vector: {np.linalg.norm(unit_v)}")

print(is_unit_vector(v))          # False
print(is_unit_vector(unit_v))     # True

zero_vector = np.array([0, 0])
print(normalize(zero_vector))     # [0 0] — I avoid dividing by zero

