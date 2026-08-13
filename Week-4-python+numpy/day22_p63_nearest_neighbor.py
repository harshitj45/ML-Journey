# ============================================
# Day 22 - Program 63
# Topic: Nearest Neighbor Finder using Broadcasting
# Concepts: broadcasting, axis parameter,
#           vectorized distance calculation
# ============================================

import numpy as np


def distances_to_all(query: np.ndarray, points: np.ndarray) -> np.ndarray:
    # I calculate the distance from one query point to
    # every point in the dataset at once, using broadcasting
    # instead of writing a loop.
    diffs = points - query
    return np.linalg.norm(diffs, axis=1)


def find_nearest(query: np.ndarray, points: np.ndarray) -> dict:
    # I find the closest point to the query and return
    # its index and distance.
    dists = distances_to_all(query, points)
    nearest_index = np.argmin(dists)
    return {
        "index": int(nearest_index),
        "point": points[nearest_index],
        "distance": dists[nearest_index],
    }


def find_k_nearest(query: np.ndarray, points: np.ndarray, k: int) -> np.ndarray:
    # I find the indices of the k closest points to the query.
    dists = distances_to_all(query, points)
    sorted_indices = np.argsort(dists)
    return sorted_indices[:k]


# --- TESTING ---

students = np.array([
    [21, 8.5],
    [20, 9.1],
    [22, 6.5],
    [23, 7.8],
    [19, 9.5],
    [24, 6.0],
])   # [age, cgpa]

new_student = np.array([21, 8.0])

all_distances = distances_to_all(new_student, students)
print(f"Distances to every student: {all_distances}")

nearest = find_nearest(new_student, students)
print(f"Nearest student: {nearest}")

k_nearest_indices = find_k_nearest(new_student, students, k=3)
print(f"Indices of 3 nearest students: {k_nearest_indices}")

for idx in k_nearest_indices:
    print(f"Student {idx}: {students[idx]}")

