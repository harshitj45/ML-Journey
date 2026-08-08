# ============================================
# Day 18 - Program 51
# Topic: Context Managers with @contextmanager
# Concepts: contextlib.contextmanager, yield
#           as the enter/exit split point
# ============================================

import time
from contextlib import contextmanager


@contextmanager
def section_timer(section_name):
    # I use this to time and label a block of code.
    # Everything before yield runs like __enter__.
    start_time = time.time()
    print(f"I am starting section: {section_name}")

    yield   # I hand control back to the with block here.

    # Everything after yield runs like __exit__.
    elapsed = time.time() - start_time
    print(f"I finished section '{section_name}' in {elapsed:.6f}s")


@contextmanager
def log_step(step_name):
    # I use this to wrap a step with a start and end message.
    print(f"[START] {step_name}")
    yield
    print(f"[DONE]  {step_name}")


@contextmanager
def suppress_errors(error_type):
    # I use this to catch one specific error type
    # and print a message instead of crashing.
    try:
        yield
    except error_type as e:
        print(f"I suppressed a {error_type.__name__}: {e}")


# --- TESTING ---

with section_timer("Loading data"):
    data = [i for i in range(100000)]
    print(f"I loaded {len(data)} items")

print()

with log_step("Step 1: Preprocessing"):
    cleaned = [x for x in data if x % 2 == 0]
    print(f"I kept {len(cleaned)} even numbers")

with log_step("Step 2: Summarizing"):
    total = sum(cleaned)
    print(f"I calculated total: {total}")

print()

with suppress_errors(ZeroDivisionError):
    result = 10 / 0
    print("I will not reach this line")

print("I continued after suppressing the error")


