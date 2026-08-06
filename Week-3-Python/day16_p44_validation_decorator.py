# ============================================
# Day 16 - Program 44
# Topic: Input Validation Decorator
# Concepts: decorator with arguments check,
#           raising exceptions inside a decorator
# ============================================


def validate_positive(func):
    # I use this decorator to check that all
    # numeric arguments passed to a function are positive.
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"Error: {arg} is negative. Value must be positive.")
                return None
        return func(*args, **kwargs)
    return wrapper


def validate_types(func):
    # I use this decorator to check that all
    # arguments are either int or float.
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                print(f"Error: {arg} is not a number.")
                return None
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def calculate_area(length, width):
    # I calculate the area of a rectangle.
    return length * width


@validate_types
def divide(a, b):
    # I divide the first number by the second.
    if b == 0:
        print("Error: cannot divide by zero.")
        return None
    return a / b


# --- TESTING ---

print("=== validate_positive ===")
print(calculate_area(5, 4))     # 20
print(calculate_area(-5, 4))    # Error message, None

print("\n=== validate_types ===")
print(divide(10, 2))            # 5.0
print(divide(10, "a"))          # Error message, None
print(divide(10, 0))            # Error message, None


