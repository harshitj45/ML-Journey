# ============================================
# Day 24 - Program 67
# Topic: Descriptive Statistics and Skewness
# Concepts: np.mean/median, mode via Counter,
#           population vs sample variance,
#           skewness calculation and interpretation
# ============================================

import numpy as np
from collections import Counter


def find_mode(data: np.ndarray) -> float:
    # I count how often each value appears and
    # return the most frequent one.
    counts = Counter(data)
    return counts.most_common(1)[0][0]


def get_variance(data: np.ndarray, is_sample: bool = True) -> float:
    # I calculate variance. I use ddof=1 for a sample
    # and ddof=0 for a full population.
    ddof = 1 if is_sample else 0
    return np.var(data, ddof=ddof)


def calculate_skewness(data: np.ndarray) -> float:
    # I calculate skewness using the standardized
    # third moment of the data.
    mean = np.mean(data)
    std = np.std(data)
    return np.mean(((data - mean) / std) ** 3)


def interpret_skewness(skew_value: float) -> str:
    # I translate a skewness number into a readable description.
    if skew_value > 0.5:
        return "right-skewed (positive) — long tail on the right"
    elif skew_value < -0.5:
        return "left-skewed (negative) — long tail on the left"
    else:
        return "roughly symmetric"


def full_summary(data: np.ndarray) -> dict:
    # I build a complete descriptive summary of a dataset.
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "mode": find_mode(data),
        "sample_variance": get_variance(data, is_sample=True),
        "sample_std": np.std(data, ddof=1),
        "skewness": calculate_skewness(data),
    }


# --- TESTING ---

marks = np.array([85, 92, 78, 95, 60, 85, 88])
summary = full_summary(marks)
for key, value in summary.items():
    print(f"{key}: {value:.3f}" if isinstance(value, float) else f"{key}: {value}")

print(interpret_skewness(summary["skewness"]))

# I test with a right-skewed salary dataset.
salaries = np.array([25000, 28000, 30000, 32000, 29000, 500000])
salary_skew = calculate_skewness(salaries)
print(f"Salary skewness: {salary_skew:.3f}")
print(interpret_skewness(salary_skew))



