# ============================================
# Day 16 - Program 45
# Topic: Stacking Multiple Decorators
# Concepts: multiple decorators on one function,
#           decorator execution order,
#           func.__name__ usage
# ============================================


def uppercase(func):
    # I convert the returned string to uppercase.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def add_exclamation(func):
    # I add an exclamation mark at the end of the result.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!"
    return wrapper


def print_call(func):
    # I print a message every time the function is called.
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} is being called")
        return func(*args, **kwargs)
    return wrapper


# Order matters — decorators apply bottom to top.
@print_call
@uppercase
@add_exclamation
def create_message(name):
    # I build a simple welcome message.
    return f"welcome {name}"


@print_call
@add_exclamation
@uppercase
def create_message_v2(name):
    # I build the same message but with decorator
    # order swapped, to compare the output.
    return f"welcome {name}"


# --- TESTING ---

print("=== Order 1: print_call -> uppercase -> add_exclamation ===")
print(create_message("Harshit"))

print("\n=== Order 2: print_call -> add_exclamation -> uppercase ===")
print(create_message_v2("Harshit"))


