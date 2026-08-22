# ============================================
# Day 24 - Program 69
# Topic: Z-Score Standardization and Outlier Detection
# Concepts: z-score formula, standardization,
#           threshold-based outlier detection
# ============================================

import numpy as np


def calculate_z_scores(data: np.ndarray) -> np.ndarray:
    # I convert every value into how many standard
    # deviations it is away from the mean.
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / std


def standardize(data: np.ndarray) -> np.ndarray:
    # I standardize the data so the result always has
    # a mean of 0 and a standard deviation of 1.
    return calculate_z_scores(data)


def find_outliers(data: np.ndarray, threshold: float = 2.0) -> np.ndarray:
    # I flag any value whose z-score magnitude is above
    # the threshold as an outlier.
    z_scores = calculate_z_scores(data)
    return data[np.abs(z_scores) > threshold]


def remove_outliers(data: np.ndarray, threshold: float = 2.0) -> np.ndarray:
    # I return the data with outliers removed instead of
    # just flagged, using the same z-score threshold.
    z_scores = calculate_z_scores(data)
    return data[np.abs(z_scores) <= threshold]


# --- TESTING ---

marks = np.array([85, 92, 78, 95, 60, 45, 88, 91])

z_scores = calculate_z_scores(marks)
print(f"Z-scores: {z_scores}")

standardized = standardize(marks)
print(f"Standardized mean: {standardized.mean():.4f}")
print(f"Standardized std: {standardized.std():.4f}")

outliers = find_outliers(marks, threshold=1.5)
print(f"Outliers found: {outliers}")

clean_data = remove_outliers(marks, threshold=1.5)
print(f"Data after removing outliers: {clean_data}")

# I test with a dataset that has one extreme value.
salaries = np.array([28000, 30000, 32000, 29000, 31000, 250000])
salary_outliers = find_outliers(salaries, threshold=1.5)
print(f"Salary outliers: {salary_outliers}")

