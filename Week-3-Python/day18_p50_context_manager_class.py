# ============================================
# Day 18 - Program 50
# Topic: Custom Context Manager (Class-based)
# Concepts: __enter__, __exit__, with statement,
#           error suppression via __exit__
# ============================================

import time


class Timer:
    # I use this context manager to measure how long
    # the code inside a with block takes to run.

    def __enter__(self):
        self.start_time = time.time()
        print("I am starting the timer.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start_time
        print(f"I stopped the timer: {elapsed:.6f} seconds")
        return False   # I do not suppress any errors here.


class SafeBlock:
    # I use this context manager to catch and report
    # a specific error type without crashing the program.

    def __enter__(self):
        print("I am entering the safe block.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ZeroDivisionError:
            print(f"I caught a division error: {exc_value}")
            return True   # I suppress this specific error.
        if exc_type is ValueError:
            print(f"I caught a value error: {exc_value}")
            return True
        return False   # I let any other error pass through.


# --- TESTING ---

with Timer() as t:
    total = 0
    for i in range(500000):
        total += i
    print(f"I calculated the total: {total}")


print()

with SafeBlock():
    print(10 / 2)
    print(10 / 0)          # this error gets caught
    print("I will not reach this line")

print("I reached this line — the program did not crash")

print()

with SafeBlock():
    print(int("abc"))      # this ValueError gets caught

print("I reached the end of the program normally")



