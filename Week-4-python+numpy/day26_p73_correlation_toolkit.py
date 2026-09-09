# ============================================
# Day 26 - Program 73
# Topic: Spearman Correlation and Confounding Variables
# Concepts: rank-based correlation, Pearson vs Spearman,
#           detecting confounding relationships
# ============================================

import numpy as np


def rank_data(data: np.ndarray) -> np.ndarray:
    # I convert raw values into their ranks, where 1 is
    # the smallest value.
    temp = data.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(1, len(data) + 1)
    return ranks


def spearman_correlation(x: np.ndarray, y: np.ndarray) -> float:
    # I calculate Spearman's rank correlation using the
    # difference between ranks instead of raw values.
    rank_x = rank_data(x)
    rank_y = rank_data(y)
    d = rank_x - rank_y
    n = len(x)
    return 1 - (6 * np.sum(d ** 2)) / (n * (n ** 2 - 1))


def pearson_correlation(x: np.ndarray, y: np.ndarray) -> float:
    # I calculate Pearson correlation using NumPy.
    return np.corrcoef(x, y)[0, 1]


def compare_correlations(x: np.ndarray, y: np.ndarray) -> dict:
    # I return both correlation types together so I can
    # compare how they respond to the same data.
    return {
        "pearson": pearson_correlation(x, y),
        "spearman": spearman_correlation(x, y),
    }


# --- TESTING ---

# I test with a monotonic but non-linear (curved) relationship.
hours_studied = np.array([1, 2, 3, 4, 5])
score = np.array([10, 25, 45, 70, 100])

result = compare_correlations(hours_studied, score)
print(f"Curved relationship: {result}")

# I test with an outlier present.
x = np.array([1, 2, 3, 4, 5])
y_with_outlier = np.array([2, 4, 6, 8, 100])

result_outlier = compare_correlations(x, y_with_outlier)
print(f"With outlier: {result_outlier}")

# I check for a possible confounding variable.
temperature = np.array([20, 25, 30, 35, 40])
ice_cream_sales = np.array([10, 25, 45, 70, 95])
drowning_incidents = np.array([2, 5, 9, 14, 19])

print(f"Ice cream vs drowning: {pearson_correlation(ice_cream_sales, drowning_incidents):.4f}")
print(f"Temperature vs ice cream: {pearson_correlation(temperature, ice_cream_sales):.4f}")
print(f"Temperature vs drowning: {pearson_correlation(temperature, drowning_incidents):.4f}")

