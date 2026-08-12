# ============================================
# Day 21 - Program 58 (Package Module)
# Topic: Batch Generator
# Concepts: yield, generator function, slicing
# ============================================

import numpy as np


def batch_generator(data: np.ndarray, batch_size: int):
    # I yield slices of the array one batch at a time
    # instead of returning everything at once.
    start = 0
    total_rows = data.shape[0]

    while start < total_rows:
        yield data[start:start + batch_size]
        start += batch_size

