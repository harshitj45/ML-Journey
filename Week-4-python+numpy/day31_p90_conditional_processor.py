# ============================================
# Day 31 - Program 90
# Topic: np.where and np.unique
# Concepts: conditional replacement, finding indices,
#           unique values, value counts
# ============================================

import numpy as np


def find_passing_indices(marks: np.ndarray, passing_mark: int = 50) -> np.ndarray:
    # I find the indices of all students who passed.
    return np.where(marks >= passing_mark)[0]


def assign_pass_fail(marks: np.ndarray, passing_mark: int = 50) -> np.ndarray:
    # I label every mark as Pass or Fail using np.where.
    return np.where(marks >= passing_mark, "Pass", "Fail")


def apply_bonus(marks: np.ndarray, threshold: int, bonus: int) -> np.ndarray:
    # I add a bonus only to marks above a threshold,
    # leaving the rest unchanged.
    return np.where(marks >= threshold, marks + bonus, marks)


def get_unique_grades(grades: np.ndarray) -> dict:
    # I find every unique grade and how many times
    # each one appears.
    unique_vals, counts = np.unique(grades, return_counts=True)
    return dict(zip(unique_vals, counts))


# --- TESTING ---

marks = np.array([45, 85, 92, 38, 78, 95, 60])

passing_idx = find_passing_indices(marks)
print(f"Indices of passing students: {passing_idx}")

labels = assign_pass_fail(marks)
print(f"Pass/Fail labels: {labels}")

boosted = apply_bonus(marks, threshold=90, bonus=5)
print(f"Marks after bonus: {boosted}")

grades = np.array(["A", "B", "A", "C", "B", "A", "C", "B"])
grade_counts = get_unique_grades(grades)
print(f"Grade distribution: {grade_counts}")

# I combine everything into one small report.
departments = np.array(["CSE", "ECE", "CSE", "ME", "CSE", "ECE"])
unique_depts = np.unique(departments)
print(f"Unique departments: {unique_depts}")

