# ============================================
# Day 24 - Program 68
# Topic: Normal and Binomial Distribution Simulation
# Concepts: np.random.normal, np.random.binomial,
#           68-95-99.7 rule verification
# ============================================

import numpy as np


def generate_normal_samples(mean: float, std: float, size: int) -> np.ndarray:
    # I generate samples from a normal distribution
    # with the given mean and standard deviation.
    return np.random.normal(loc=mean, scale=std, size=size)


def verify_empirical_rule(data: np.ndarray) -> dict:
    # I check what percentage of the data falls within
    # 1, 2, and 3 standard deviations of the mean.
    mean = np.mean(data)
    std = np.std(data)
    n = len(data)

    within_1 = np.sum((data >= mean - std) & (data <= mean + std)) / n * 100
    within_2 = np.sum((data >= mean - 2*std) & (data <= mean + 2*std)) / n * 100
    within_3 = np.sum((data >= mean - 3*std) & (data <= mean + 3*std)) / n * 100

    return {"within_1_std": within_1, "within_2_std": within_2, "within_3_std": within_3}


def simulate_pass_rate(n_students: int, pass_probability: float, trials: int) -> np.ndarray:
    # I simulate how many students pass out of n_students,
    # repeated across many trials, using a binomial distribution.
    return np.random.binomial(n=n_students, p=pass_probability, size=trials)


def compare_theoretical_vs_empirical(n: int, p: float, trials: int) -> dict:
    # I compare the theoretical expected value with what
    # I actually observe from simulation.
    results = simulate_pass_rate(n, p, trials)
    return {
        "theoretical_average": n * p,
        "empirical_average": results.mean(),
    }


# --- TESTING ---

np.random.seed(42)

marks = generate_normal_samples(mean=70, std=10, size=10000)
print(f"Generated mean: {marks.mean():.2f}, std: {marks.std():.2f}")

rule_check = verify_empirical_rule(marks)
for key, value in rule_check.items():
    print(f"{key}: {value:.2f}%")

comparison = compare_theoretical_vs_empirical(n=10, p=0.7, trials=1000)
print(f"Theoretical average passes: {comparison['theoretical_average']}")
print(f"Empirical average passes: {comparison['empirical_average']:.2f}")