# ============================================
# Day 29 - Program 83
# Topic: Similar Student Finder (Synthesis)
# Concepts: decorators, generators, cosine similarity,
#           combining Week 3 and Week 4 concepts
# ============================================

import time
import numpy as np


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.6f}s")
        return result
    return wrapper


def batch_generator(data: np.ndarray, batch_size: int):
    start = 0
    while start < len(data):
        yield data[start:start + batch_size]
        start += batch_size


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@timer
def find_most_similar(query: np.ndarray, dataset: np.ndarray, batch_size: int = 2) -> dict:
    best_score = -2
    best_index = -1
    global_index = 0

    for batch in batch_generator(dataset, batch_size):
        for row in batch:
            score = cosine_similarity(query, row)
            if score > best_score:
                best_score = score
                best_index = global_index
            global_index += 1

    return {"index": best_index, "score": best_score}


# --- TESTING ---
students = np.array([
    [21, 8.5, 5], [20, 9.1, 6], [22, 6.5, 3],
    [23, 7.8, 4], [19, 9.5, 7],
])
query_student = np.array([21, 8.7, 5])

result = find_most_similar(query_student, students, batch_size=2)
print(result)


