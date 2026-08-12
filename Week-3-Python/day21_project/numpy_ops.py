# ============================================
# Day 21 - Program 59
# Topic: NumPy Vector and Matrix Operations
# Concepts: dot product, norm, matrix multiply,
#           type hints with np.ndarray
# ============================================

import numpy as np


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    # I calculate the dot product of two vectors.
    return np.dot(v1, v2)


def euclidean_distance(p1: np.ndarray, p2: np.ndarray) -> float:
    # I calculate the straight-line distance between two points.
    return np.linalg.norm(p2 - p1)


def normalize_batch(batch: np.ndarray, max_value: float) -> np.ndarray:
    # I scale every value in the batch down using a known max value.
    return batch / max_value


def predict_batch(batch: np.ndarray, weights: np.ndarray) -> np.ndarray:
    # I calculate predictions for an entire batch at once
    # using matrix multiplication instead of a loop.
    return batch @ weights

