from functools import reduce

def add(*args):
    """Add any number of values."""
    return sum(args)

def subtract(*args):
    """Subtract all from first value."""
    if len(args) == 0:
        raise ValueError("At least one value required!")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Multiply all values."""
    if len(args) == 0:
        return 1
    return reduce(lambda a, b: a * b, args, 1)

def divide(*args):
    """Divide first by all subsequent."""
    if len(args) == 0:
        raise ValueError("At least one value required!")
    if 0 in args[1:]:
        raise ZeroDivisionError(
            "Cannot divide by zero!"
        )
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

def power(base, *exponents):
    """Apply exponents sequentially."""
    result = base
    for exp in exponents:
        result = result ** exp
    return result

def calculate(operation, *nums):
    """
    Master calculator function.
    Calls appropriate operation.
    """
    operations = {
        "add":      add,
        "subtract": subtract,
        "multiply": multiply,
        "divide":   divide,
        "power":    power,
    }

    if operation not in operations:
        raise ValueError(
            f"Unknown operation: {operation}\n"
            f"Available: {list(operations.keys())}"
        )

    try:
        result = operations[operation](*nums)
        print(f"  {operation}{nums} = {result}")
        return result
    except ZeroDivisionError as e:
        print(f"  ❌ Error: {e}")
        return None
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return None

# Tests:
print("=" * 40)
print("    CALCULATOR TESTS")
print("=" * 40)

calculate("add", 1, 2, 3, 4, 5)        # 15
calculate("subtract", 100, 20, 15, 5)  # 60
calculate("multiply", 2, 3, 4)         # 24
calculate("divide", 100, 2, 5)         # 10.0
calculate("divide", 10, 0)             # Error
calculate("power", 2, 3)               # 8
calculate("power", 2, 2, 3)            # 64 (2²=4, 4³=64)


#=====================================================================================


# Bonus: Statistics calculator
def stats(*numbers):
    """Calculate statistics for any numbers."""
    n = len(numbers)
    if n == 0:
        return None

    total = sum(numbers)
    mean  = total / n

    # Variance
    variance = sum(
        (x - mean) ** 2
        for x in numbers
    ) / n
    std_dev = variance ** 0.5

    sorted_nums = sorted(numbers)
    median = (sorted_nums[n//2]
              if n % 2 != 0
              else (sorted_nums[n//2 - 1] +
                    sorted_nums[n//2]) / 2)

    print(f"\nStatistics for {numbers}:")
    print(f"  Count   : {n}")
    print(f"  Sum     : {total}")
    print(f"  Mean    : {mean:.2f}")
    print(f"  Median  : {median}")
    print(f"  Std Dev : {std_dev:.2f}")
    print(f"  Min     : {min(numbers)}")
    print(f"  Max     : {max(numbers)}")

stats(85, 92, 78, 95, 60, 88, 72)
