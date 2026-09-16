# ============================================
# Day 31 - Program 89
# Topic: Fancy Indexing and Boolean Masking
# Concepts: index arrays, reordering, row selection,
#           combining conditions with & | ~
# ============================================

import numpy as np


def select_by_index(data: np.ndarray, indices: list) -> np.ndarray:
    # I select specific elements using a list of indices.
    return data[indices]


def reorder_data(data: np.ndarray, new_order: list) -> np.ndarray:
    # I reorder data into any custom sequence I choose.
    return data[new_order]


def select_rows(matrix: np.ndarray, row_indices: list) -> np.ndarray:
    # I select specific rows from a 2D array.
    return matrix[row_indices]


def filter_range(data: np.ndarray, low: float, high: float) -> np.ndarray:
    # I filter values that fall inside a range using
    # boolean indexing with combined conditions.
    return data[(data >= low) & (data <= high)]


def filter_outside_range(data: np.ndarray, low: float, high: float) -> np.ndarray:
    # I filter values that fall outside a range using
    # the NOT operator on a combined condition.
    return data[~((data >= low) & (data <= high))]


# --- TESTING ---

scores = np.array([45, 85, 92, 38, 78, 95, 60])

# Fancy indexing — selection and reordering.
top_three = select_by_index(scores, [2, 5, 1])
print(f"Top three by index: {top_three}")

custom_order = reorder_data(scores, [6, 0, 3])
print(f"Custom order: {custom_order}")

# 2D fancy indexing on a student dataset.
students = np.array([
    [85, 90], [45, 50], [92, 88], [38, 42], [78, 80]
])
chosen_students = select_rows(students, [0, 2, 4])
print(f"Chosen students:\n{chosen_students}")

# Boolean indexing — combined conditions.
mid_range = filter_range(scores, 50, 90)
print(f"Scores between 50-90: {mid_range}")

extremes = filter_outside_range(scores, 50, 90)
print(f"Scores outside 50-90: {extremes}")
