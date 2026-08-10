# ============================================
# Day 19 - Program 53
# Topic: Sigma Notation as Python Formulas
# Concepts: sum(), generator expressions,
#           implementing math formulas in code
# ============================================


def summation(numbers: list) -> float:
    # I implement Sigma — I add up all the numbers.
    return sum(numbers)


def sum_of_squares(numbers: list) -> float:
    # I implement Sigma(x_i squared).
    return sum(x ** 2 for x in numbers)


def average(numbers: list) -> float:
    # I implement (1/n) * Sigma(x_i), the mean formula.
    n = len(numbers)
    return summation(numbers) / n


def mean_squared_error(predictions: list, actuals: list) -> float:
    # I implement MSE = (1/n) * Sigma((pred - actual) squared).
    n = len(predictions)
    total_error = sum(
        (p - a) ** 2
        for p, a in zip(predictions, actuals)
    )
    return total_error / n


def variance(numbers: list) -> float:
    # I implement variance = (1/n) * Sigma((x_i - mean) squared).
    n = len(numbers)
    mean_value = average(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / n


# --- TESTING ---

marks = [85, 92, 78, 95, 60]

print(summation(marks))            # 410
print(sum_of_squares(marks))       # 34438
print(average(marks))               # 82.0
print(variance(marks))              # 145.6

predictions = [8, 5, 9, 12]
actuals     = [10, 6, 8, 11]

print(mean_squared_error(predictions, actuals))

