# ============================================
# Day 28 - Program 79 (Utility Module)
# Topic: Reusable Maths for ML Toolkit
# Concepts: dot product, norms, cosine similarity,
#           standardization, correlation — all
#           collected from Week 3-4 into one module
# ============================================

import numpy as np


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    # I calculate the dot product of two vectors.
    return np.dot(a, b)


def l2_norm(v: np.ndarray) -> float:
    # I calculate the L2 norm, the vector's length.
    return np.linalg.norm(v)


def l1_norm(v: np.ndarray) -> float:
    # I calculate the L1 norm, the sum of absolute values.
    return np.sum(np.abs(v))


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # I measure how similar two vectors' directions are.
    return dot_product(a, b) / (l2_norm(a) * l2_norm(b))


def standardize(data: np.ndarray) -> dict:
    # I convert data into z-scores, and I also return the
    # mean and std so I can apply the exact same
    # transformation to new data later.
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std
    return {"data": standardized_data, "mean": mean, "std": std}


def apply_standardization(data: np.ndarray, mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    # I standardize new data using previously stored
    # mean and std, instead of recalculating them.
    return (data - mean) / std


def correlation(x: np.ndarray, y: np.ndarray) -> float:
    # I calculate the Pearson correlation between two arrays.
    return np.corrcoef(x, y)[0, 1]


def r_squared(y_actual: np.ndarray, y_predicted: np.ndarray) -> float:
    # I calculate the R-squared score to measure how well
    # predictions match the actual values.
    ss_res = np.sum((y_actual - y_predicted) ** 2)
    ss_tot = np.sum((y_actual - np.mean(y_actual)) ** 2)
    return 1 - (ss_res / ss_tot)


def numerical_derivative(func, x: float, h: float = 1e-6) -> float:
    # I approximate a derivative using finite differences,
    # useful for verifying manually computed gradients.
    return (func(x + h) - func(x - h)) / (2 * h)

