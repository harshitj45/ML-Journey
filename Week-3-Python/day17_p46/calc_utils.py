# ============================================
# Day 17 - Program 46 (Module File)
# Topic: Custom Math Utilities Module
# Concepts: module functions, importable code
# ============================================


def add(a, b):
    # I add two numbers and return the result.
    return a + b


def subtract(a, b):
    # I subtract the second number from the first.
    return a - b


def multiply(a, b):
    # I multiply two numbers together.
    return a * b


def divide(a, b):
    # I divide the first number by the second.
    # I return None if the divisor is zero.
    if b == 0:
        print("I cannot divide by zero.")
        return None
    return a / b


def average(numbers):
    # I calculate the average of a list of numbers.
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# I use this guard so my test prints only run
# when I execute this file directly, not when
# another file imports it.
if __name__ == "__main__":
    print("Testing calc_utils.py directly")
    print(add(5, 3))
    print(average([10, 20, 30]))

