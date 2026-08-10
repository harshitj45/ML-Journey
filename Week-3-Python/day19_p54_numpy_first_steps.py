# ============================================
# Day 19 - Program 54
# Topic: NumPy Arrays — First Steps
# Concepts: np.array, indexing, slicing,
#           vectorized operations, sum, mean
# ============================================

import numpy as np


def make_array(numbers: list) -> np.ndarray:
    # I convert a regular Python list into a NumPy array.
    return np.array(numbers)


def add_bonus(marks: np.ndarray, bonus: int) -> np.ndarray:
    # I add bonus marks to every element at once.
    # I do not need a loop for this — NumPy applies it
    # to the whole array in one step.
    return marks + bonus


def to_percentage(marks: np.ndarray, total: int) -> np.ndarray:
    # I convert marks into percentages for every element.
    return (marks / total) * 100


def get_stats(marks: np.ndarray) -> dict:
    # I calculate basic statistics using NumPy's
    # built-in methods instead of writing my own loops.
    return {
        "sum": marks.sum(),
        "mean": marks.mean(),
        "min": marks.min(),
        "max": marks.max(),
    }


# --- TESTING ---

marks_list = [85, 92, 78, 95, 60]
marks = make_array(marks_list)

print(type(marks))          # numpy.ndarray
print(marks.shape)          # (5,)
print(marks.dtype)          # int64

# Indexing — same as list indexing:
print(marks[0])             # 85
print(marks[-1])            # 60
print(marks[1:3])           # [92 78]

# Vectorized operations — no loop needed:
bonus_marks = add_bonus(marks, 5)
print(bonus_marks)          # [90 97 83 100 65]

percentages = to_percentage(marks, 100)
print(percentages)          # [85. 92. 78. 95. 60.]

stats = get_stats(marks)
print(stats)

