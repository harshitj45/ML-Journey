# ============================================
# Day 31 - Program 88
# Topic: Detecting Views vs Copies
# Concepts: np.shares_memory, .base attribute,
#           basic slicing vs fancy/boolean indexing,
#           explicit .copy()
# ============================================

import numpy as np


def is_view(original: np.ndarray, subset: np.ndarray) -> bool:
    # I check whether a subset shares memory with the
    # original array, which tells me if it is a view.
    return np.shares_memory(original, subset)


def check_base(subset: np.ndarray) -> bool:
    # I check the base attribute. If base is None, the
    # array owns its own data, meaning it is a copy.
    return subset.base is None


def safe_slice(arr: np.ndarray, start: int, stop: int) -> np.ndarray:
    # I force a copy of a slice so the original array
    # is never affected, even though slicing alone
    # would normally give me a view.
    return arr[start:stop].copy()


def classify_selection(original: np.ndarray, subset: np.ndarray) -> str:
    # I classify a selection as a view or a copy using
    # both detection methods together.
    shares_memory = is_view(original, subset)
    owns_data = check_base(subset)
    if shares_memory and not owns_data:
        return "VIEW"
    return "COPY"


# --- TESTING ---

arr = np.arange(10)

basic_slice = arr[2:5]
fancy_selection = arr[[2, 3, 4]]
boolean_selection = arr[arr > 5]
reshaped = arr.reshape(2, 5)

print(f"Basic slice: {classify_selection(arr, basic_slice)}")
print(f"Fancy indexing: {classify_selection(arr, fancy_selection)}")
print(f"Boolean indexing: {classify_selection(arr, boolean_selection)}")
print(f"Reshape: {classify_selection(arr, reshaped)}")

# I demonstrate the safe_slice function protecting the original.
protected = safe_slice(arr, 2, 5)
protected[0] = -999
print(f"Original after safe_slice edit: {arr}")
print(f"Protected copy: {protected}")

# I demonstrate the risk of an unprotected slice.
risky = arr[2:5]
risky[0] = -999
print(f"Original after unprotected slice edit: {arr}")

