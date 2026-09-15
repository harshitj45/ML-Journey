# ============================================
# Day 30 - Program 85
# Topic: NumPy Array Creation Functions
# Concepts: zeros, ones, full, eye, arange,
#           linspace, dtype control
# ============================================

import numpy as np


def make_placeholder(shape: tuple, fill_value: float = 0) -> np.ndarray:
    # I create an array of a given shape filled with one value.
    return np.full(shape, fill_value)


def make_identity(size: int) -> np.ndarray:
    # I create an identity matrix of the given size.
    return np.eye(size)


def make_integer_zeros(length: int) -> np.ndarray:
    # I create a zero array with integer dtype instead
    # of the default float dtype.
    return np.zeros(length, dtype=int)


def make_range(start: float, stop: float, step: float) -> np.ndarray:
    # I create a range where I control the step size.
    return np.arange(start, stop, step)


def make_evenly_spaced(start: float, stop: float, count: int) -> np.ndarray:
    # I create evenly spaced points where I control
    # the total count, and the stop value is included.
    return np.linspace(start, stop, count)


# --- TESTING ---

grid = make_placeholder((3, 3), fill_value=9)
print(grid)

identity = make_identity(4)
print(identity)

int_zeros = make_integer_zeros(5)
print(int_zeros)
print(int_zeros.dtype)

step_range = make_range(0, 20, 4)
print(step_range)

count_range = make_evenly_spaced(0, 20, 4)
print(count_range)

# I compare arange vs linspace on the same interval.
a = np.arange(0, 1, 0.25)
b = np.linspace(0, 1, 4)
print(f"arange: {a}")
print(f"linspace: {b}")

