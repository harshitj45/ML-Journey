# ============================================
# Day 32 - Program 92 (Module)
# Topic: Cleaning Data with Boolean and Fancy Indexing
# Concepts: boolean masking with & | ~,
#           z-score outlier detection, np.where,
#           fancy indexing for reordering
# ============================================

import numpy as np


def remove_invalid_hours(dataset: np.ndarray, hours_col: int = 1) -> np.ndarray:
    # I remove any row where hours_studied is negative,
    # since that is not a physically valid value.
    valid_mask = dataset[:, hours_col] >= 0
    return dataset[valid_mask]


def remove_outliers_by_zscore(dataset: np.ndarray, col: int, threshold: float = 2.0) -> np.ndarray:
    # I remove rows where a column's z-score is too extreme,
    # reusing the z-score idea from Day 24.
    column = dataset[:, col]
    mean = np.mean(column)
    std = np.std(column)
    z_scores = (column - mean) / std
    keep_mask = np.abs(z_scores) <= threshold
    return dataset[keep_mask]


def label_performance(dataset: np.ndarray, marks_col: int) -> np.ndarray:
    # I label every student as High or Low performer
    # using np.where, based on their marks.
    marks = dataset[:, marks_col]
    return np.where(marks >= 75, "High", "Low")


def reorder_by_marks(dataset: np.ndarray, marks_col: int) -> np.ndarray:
    # I reorder the dataset from highest to lowest marks
    # using fancy indexing with argsort.
    order = np.argsort(dataset[:, marks_col])[::-1]
    return dataset[order]


def full_clean(dataset: np.ndarray, hours_col: int, marks_col: int) -> np.ndarray:
    # I run every cleaning step together, in sequence.
    step1 = remove_invalid_hours(dataset, hours_col)
    step2 = remove_outliers_by_zscore(step1, marks_col)
    step3 = reorder_by_marks(step2, marks_col)
    return step3

