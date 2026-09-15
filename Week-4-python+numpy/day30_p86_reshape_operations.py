# ============================================
# Day 30 - Program 86
# Topic: Reshaping, Flattening, and Views vs Copies
# Concepts: reshape, -1 auto-dimension,
#           flatten (copy) vs ravel (view)
# ============================================

import numpy as np


def reshape_to_grid(flat_array: np.ndarray, rows: int, cols: int) -> np.ndarray:
    # I reshape a flat array into a grid of the given size.
    return flat_array.reshape(rows, cols)


def reshape_auto(flat_array: np.ndarray, rows: int) -> np.ndarray:
    # I reshape into a fixed number of rows, letting NumPy
    # figure out the column count automatically.
    return flat_array.reshape(rows, -1)


def safe_flatten(matrix: np.ndarray) -> np.ndarray:
    # I flatten using flatten(), which always returns a
    # copy, so editing this result never affects the original.
    return matrix.flatten()


def fast_flatten(matrix: np.ndarray) -> np.ndarray:
    # I flatten using ravel(), which returns a view when
    # possible — faster, but editing this CAN affect the original.
    return matrix.ravel()


def demonstrate_view_vs_copy(matrix: np.ndarray) -> dict:
    # I show the difference between flatten and ravel by
    # editing each result and checking if the original changed.
    original_copy = matrix.copy()

    flat_copy = safe_flatten(matrix)
    flat_copy[0] = -1
    flatten_changed_original = not np.array_equal(matrix, original_copy)

    matrix2 = original_copy.copy()
    flat_view = fast_flatten(matrix2)
    flat_view[0] = -1
    ravel_changed_original = not np.array_equal(matrix2, original_copy)

    return {
        "flatten_changed_original": flatten_changed_original,
        "ravel_changed_original": ravel_changed_original,
    }


# --- TESTING ---

pixels = np.arange(9)
image = reshape_to_grid(pixels, 3, 3)
print(image)

data = np.arange(20)
auto_shaped = reshape_auto(data, 4)
print(auto_shaped.shape)

matrix = np.array([[1, 2], [3, 4]])
result = demonstrate_view_vs_copy(matrix)
print(result)

