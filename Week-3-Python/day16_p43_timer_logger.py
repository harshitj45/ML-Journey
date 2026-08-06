# ============================================
# Day 16 - Program 43
# Topic: Timer and Logger Decorators
# Concepts: decorator basics, *args/**kwargs,
#           func.__name__, wrapper function
# ============================================

import time


def timer(func):
    # I use this decorator to measure how long
    # a function takes to run.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def logger(func):
    # I use this decorator to print which function
    # is being called and with what arguments.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@timer
def calculate_sum(n):
    # I add up numbers from 0 to n-1.
    total = 0
    for i in range(n):
        total += i
    return total


@logger
def add(a, b):
    # I add two numbers together.
    return a + b


@logger
def greet(name, greeting="Hello"):
    # I create a greeting message.
    return f"{greeting}, {name}!"


# --- TESTING ---

print("=== Timer Decorator ===")
calculate_sum(1000000)

print("\n=== Logger Decorator ===")
add(5, 3)

print()
greet("Harshit")
greet("Priya", greeting="Hi")


