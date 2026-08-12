# ============================================
# Day 21 - Program 60
# Topic: Week 3 Mini Project - Main Pipeline
# Concepts: package import, generator, decorator,
#           context manager, NumPy operations
#           - all Week 3 concepts combined
# ============================================

import time
import numpy as np
from contextlib import contextmanager

from pipeline_tools.decorators import timer
from pipeline_tools.batch_generator import batch_generator
from numpy_ops import dot_product, euclidean_distance, normalize_batch, predict_batch


@contextmanager
def pipeline_run(name: str):
    # I wrap the whole pipeline run with a start and end message,
    # and I report the total time it took.
    print(f"I am starting pipeline: {name}")
    start_time = time.time()

    yield   # I hand control back to the with block here.

    elapsed = time.time() - start_time
    print(f"I finished pipeline '{name}' in {elapsed:.4f} seconds")


@timer
def process_batch(batch: np.ndarray, weights: np.ndarray) -> np.ndarray:
    # I process one batch and return its predictions.
    # The timer decorator reports how long this call takes.
    return predict_batch(batch, weights)


# --- TESTING ---

student_data = np.array([
    [21, 8.5, 5],
    [20, 9.1, 6],
    [22, 6.5, 3],
    [23, 7.8, 4],
    [19, 9.5, 7],
    [24, 6.0, 2],
])

feature_weights = np.array([0.1, 0.5, 0.4])

with pipeline_run("Student Score Prediction"):
    for i, batch in enumerate(batch_generator(student_data, batch_size=2), 1):
        print(f"I am processing batch {i}, shape {batch.shape}")
        predictions = process_batch(batch, feature_weights)
        print(f"Predictions: {predictions}")

print()

# I also demonstrate the standalone vector functions
# from numpy_ops, outside the batch pipeline.
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"Dot product: {dot_product(v1, v2)}")
print(f"Distance: {euclidean_distance(v1, v2)}")

sample_batch = student_data[:2]
print(f"Normalized batch:\n{normalize_batch(sample_batch, max_value=25)}")

