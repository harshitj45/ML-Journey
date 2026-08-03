# ============================================
# Day 13 - Program 34
# Topic: Safe Calculator with Exception Handling
# Concepts: try/except/else/finally,
#           multiple except, custom exception,
#           raise
# ============================================


# Custom exception — apni error class
class DivisionByZeroError(Exception):
    pass

class InvalidInputError(Exception):
    pass


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError(   # apni error raise karo
            "Zero se divide nahi kar sakte!"
        )
    return a / b


def calculate(num1, num2, operator):
    # Input validation
    if not isinstance(num1, (int, float)):
        raise InvalidInputError(f"{num1} number nahi hai!")
    if not isinstance(num2, (int, float)):
        raise InvalidInputError(f"{num2} number nahi hai!")

    try:
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)   # custom error aa sakti hai
        else:
            raise InvalidInputError(
                f"Operator '{operator}' unknown!"
            )

    except DivisionByZeroError as e:
        print(f"Math Error: {e}")
        return None

    except InvalidInputError as e:
        print(f"Input Error: {e}")
        return None

    else:
        # sirf tab jab koi error na aaye
        print(f"Result: {num1} {operator} {num2} = {result}")
        return result

    finally:
        # hamesha chalega
        print("--- calculation attempt done ---")


# --- TESTING ---

calculate(10, 2, "+")     # Result: 12
calculate(10, 3, "/")     # Result: 3.33
calculate(10, 0, "/")     # DivisionByZeroError
calculate(10, 2, "%")     # InvalidInputError