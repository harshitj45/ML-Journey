# ============================================
# Day 32 - Program 91 (Module)
# Topic: Combining Multiple Raw Data Sources
# Concepts: vstack, hstack, array creation,
#           reshape for adding columns
# ============================================

import numpy as np


def get_batch_a() -> np.ndarray:
    # I represent one data source — [hours_studied, attendance, marks].
    return np.array([
        [8, 95, 88],
        [3, 60, 45],
        [6, 85, 78],
        [9, 98, 92],
    ])


def get_batch_b() -> np.ndarray:
    # I represent a second data source, collected separately.
    return np.array([
        [1, 40, 250],   # I planted an obvious outlier here (marks=250)
        [7, 90, 82],
        [5, 75, 68],
    ])


def get_batch_c() -> np.ndarray:
    # I represent a third data source.
    return np.array([
        [-2, 88, 70],    # I planted a negative hours value here
        [4, 65, 55],
        [10, 100, 95],
    ])


def combine_all_sources() -> np.ndarray:
    # I stack every batch into one combined dataset.
    return np.vstack([get_batch_a(), get_batch_b(), get_batch_c()])


def add_student_ids(dataset: np.ndarray) -> np.ndarray:
    # I add a student ID column using hstack, so every
    # row can be tracked by a unique identifier.
    student_ids = np.arange(1, len(dataset) + 1).reshape(-1, 1)
    return np.hstack([student_ids, dataset])

