# ============================================
# Day 15 - Program 41
# Topic: Generator Functions with yield
# Concepts: yield, generator object,
#           next(), generator expression
# ============================================


def fibonacci(n):
    # n terms tak fibonacci numbers yield karo
    a, b  = 0, 1
    count = 0
    while count < n:
        yield a             # pause — value do
        a, b  = b, a + b    # next fibonacci
        count += 1


def squares(start, end):
    # start se end tak squares yield karo
    for n in range(start, end + 1):
        yield n ** 2        # pause — square do


def evens_only(numbers):
    # list mein se sirf even yield karo
    for n in numbers:
        if n % 2 == 0:
            yield n         # sirf even pause karo


def countdown(n):
    # n se 0 tak yield karo
    while n >= 0:
        yield n             # pause — value do
        n -= 1


# --- TESTING ---

print("Fibonacci first 8:")
for f in fibonacci(8):
    print(f, end=" ")       # 0 1 1 2 3 5 8 13
print()

print("\nSquares 1-5:")
for s in squares(1, 5):
    print(s, end=" ")       # 1 4 9 16 25
print()

print("\nEvens from list:")
nums = [1, 2, 3, 4, 5, 6, 7, 8]
for e in evens_only(nums):
    print(e, end=" ")       # 2 4 6 8
print()

print("\nCountdown from 5:")
for n in countdown(5):
    print(n, end=" ")       # 5 4 3 2 1 0
print()

# next() se manually:
print("\nnext() manually — fibonacci:")
fib = fibonacci(5)
print(next(fib))    # 0
print(next(fib))    # 1
print(next(fib))    # 1
print(next(fib))    # 2

# Generator expression:
print("\nGenerator expression — squares:")
sq_gen = (x**2 for x in range(1, 6))
print(list(sq_gen))         # [1, 4, 9, 16, 25]

# ⚠️ Ek baar hi chalta hai:
print(list(sq_gen))         # [] — khatam!



