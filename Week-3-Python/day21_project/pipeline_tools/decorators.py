# ============================================
# Day 21 - Program 58 (Package Module)
# Topic: Timer Decorator
# Concepts: decorator, wrapper, *args/**kwargs
# ============================================

import time


def timer(func):
    # I use this decorator to measure how long
    # any function takes to run.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"I finished {func.__name__} in {elapsed:.6f} seconds")
        return result
    return wrapper

