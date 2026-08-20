# ============================================
# Day 23 - Program 66
# Topic: Covariance and Correlation Matrix
# Concepts: np.cov, np.corrcoef, transpose,
#           interpreting feature relationships
# ============================================

import numpy as np


def build_covariance_matrix(data: np.ndarray) -> np.ndarray:
    # I calculate the covariance matrix. I transpose the
    # data first because np.cov expects each row to be
    # one feature, not one sample.
    return np.cov(data.T)


def build_correlation_matrix(data: np.ndarray) -> np.ndarray:
    # I calculate the correlation matrix, which is a
    # normalized version of covariance, always between -1 and 1.
    return np.corrcoef(data.T)


def get_variance_of_feature(cov_matrix: np.ndarray, feature_index: int) -> float:
    # I extract one feature's variance from the diagonal
    # of the covariance matrix.
    return cov_matrix[feature_index, feature_index]


def get_relationship(corr_matrix: np.ndarray, i: int, j: int) -> str:
    # I describe the relationship between two features
    # based on their correlation value.
    value = corr_matrix[i, j]
    if value > 0.7:
        return "strong positive relationship"
    elif value > 0.3:
        return "moderate positive relationship"
    elif value > -0.3:
        return "weak or no relationship"
    elif value > -0.7:
        return "moderate negative relationship"
    else:
        return "strong negative relationship"


# --- TESTING ---

# Dataset: [hours_studied, marks] for 5 students
student_data = np.array([
    [2, 50],
    [4, 65],
    [6, 78],
    [8, 90],
    [10, 95],
])

cov_matrix = build_covariance_matrix(student_data)
print(f"Covariance matrix:\n{cov_matrix}")

corr_matrix = build_correlation_matrix(student_data)
print(f"Correlation matrix:\n{corr_matrix}")

hours_variance = get_variance_of_feature(cov_matrix, 0)
marks_variance = get_variance_of_feature(cov_matrix, 1)
print(f"Hours variance: {hours_variance}")
print(f"Marks variance: {marks_variance}")

relationship = get_relationship(corr_matrix, 0, 1)
print(f"Hours vs Marks: {relationship}")

# I test with a dataset that has a negative relationship.
# [distance_from_college, attendance_percent]
attendance_data = np.array([
    [1, 95],
    [3, 88],
    [5, 80],
    [8, 65],
    [12, 50],
])

corr2 = build_correlation_matrix(attendance_data)
print(get_relationship(corr2, 0, 1))

