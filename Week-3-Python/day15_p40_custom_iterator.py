# ============================================
# Day 15 - Program 40
# Topic: Custom Iterator Classes
# Concepts: __iter__, __next__, StopIteration
# ============================================


class CountDown:

    def __init__(self, start):
        self.start   = start
        self.current = start        # current position

    def __iter__(self):
        # iterator return karo — self
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration     # loop band karo
        value        = self.current
        self.current -= 1           # ek kam karo
        return value


class EvenIterator:

    def __init__(self, start, end):
        # pehla even number dhundho
        self.current = start if start % 2 == 0 else start + 1
        self.end     = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value        = self.current
        self.current += 2           # agla even
        return value


class SquareIterator:

    def __init__(self, n):
        self.n       = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value        = self.current ** 2    # square karo
        self.current += 1
        return value


# --- TESTING ---

print("CountDown from 5:")
for n in CountDown(5):
    print(n, end=" ")           # 5 4 3 2 1
print()

print("\nEven numbers 1-10:")
for n in EvenIterator(1, 10):
    print(n, end=" ")           # 2 4 6 8 10
print()

print("\nSquares 1-5:")
for n in SquareIterator(5):
    print(n, end=" ")           # 1 4 9 16 25
print()

# next() manually:
print("\nManual next():")
cd = CountDown(3)
print(next(cd))     # 3
print(next(cd))     # 2
print(next(cd))     # 1
# print(next(cd))   # StopIteration!


