# ============================================
# Day 22 - Program 62
# Topic: Cosine Similarity
# Concepts: dot product + norm combined,
#           direction-based comparison
# ============================================

import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # I combine the dot product and the norms of both
    # vectors to measure how similar their directions are.
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot / (norm_a * norm_b)


def most_similar(query: np.ndarray, candidates: dict) -> str:
    # I compare the query vector against every candidate
    # and return the name of the most similar one.
    best_name = None
    best_score = -2   # I start lower than the minimum possible score.

    for name, vector in candidates.items():
        score = cosine_similarity(query, vector)
        if score > best_score:
            best_score = score
            best_name = name

    return best_name


# --- TESTING ---

# I represent documents as word-presence vectors.
# Word order tracked: [machine, learning, python, cooking, recipe]

doc_ml_python   = np.array([1, 1, 1, 0, 0])
doc_ml_only     = np.array([1, 1, 0, 0, 0])
doc_cooking     = np.array([0, 0, 0, 1, 1])

print(cosine_similarity(doc_ml_python, doc_ml_only))
print(cosine_similarity(doc_ml_python, doc_cooking))

# I check which existing document is closest to a new one.
new_doc = np.array([1, 1, 0, 0, 0])

library = {
    "ML and Python article": doc_ml_python,
    "ML basics article": doc_ml_only,
    "Cooking recipe article": doc_cooking,
}

closest = most_similar(new_doc, library)
print(f"I found the closest match: {closest}")

# I also test with product feature vectors.
product_a = np.array([5, 3, 1])   # [price_rating, quality, weight]
product_b = np.array([4, 3, 1])
product_c = np.array([1, 5, 5])

print(cosine_similarity(product_a, product_b))
print(cosine_similarity(product_a, product_c))
