import sys
from functools import lru_cache

# ─────────────────────────────────
# Part A: Classic Recursion
# ─────────────────────────────────

def factorial(n):
    """n! = n × (n-1)!"""
    if n < 0:
        raise ValueError("Negative factorial!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_digits(n):
    """
    Sum of digits.
    sum_digits(1234) → 10
    """
    n = abs(n)           # negative handle
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

def reverse_string(s):
    """
    Reverse string recursively.
    reverse_string("hello") → "olleh"
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    """
    Check palindrome recursively.
    "racecar" → True
    """
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def power(base, exp):
    """
    base^exp recursively.
    Efficient: O(log n) not O(n)
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half           # efficient!
    return base * power(base, exp - 1)

# Tests:
print("=" * 40)
print("RECURSION TESTS")
print("=" * 40)
print(f"factorial(10)     = {factorial(10)}")
print(f"sum_digits(9875)  = {sum_digits(9875)}")
print(f"reverse('Harshit')= {reverse_string('Harshit')}")
print(f"palindrome('racecar') = {is_palindrome('racecar')}")
print(f"palindrome('hello')   = {is_palindrome('hello')}")
print(f"power(2, 10)      = {power(2, 10)}")
print(f"power(2, -3)      = {power(2, -3):.4f}")

# ─────────────────────────────────
# Part B: ML-Relevant Recursion
# ─────────────────────────────────

def binary_search(arr, target,
                  low=None, high=None):
    """O(log n) search."""
    if low is None: low = 0
    if high is None: high = len(arr) - 1

    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:   return mid
    elif arr[mid] < target:
        return binary_search(arr, target,
                             mid+1, high)
    else:
        return binary_search(arr, target,
                             low, mid-1)

def merge_sort(arr):
    """
    Merge sort — O(n log n).
    Used internally in many ML libraries.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Tests:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(f"\nmerge_sort({arr})")
print(f"= {sorted_arr}")

idx = binary_search(sorted_arr, 25)
print(f"\nbinary_search for 25: index {idx}")
idx = binary_search(sorted_arr, 100)
print(f"binary_search for 100: {idx}")

# ─────────────────────────────────
# Part C: Memoization Comparison
# ─────────────────────────────────

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_slow(n):
    if n <= 1: return n
    return fib_slow(n-1) + fib_slow(n-2)

import time

n = 35
start = time.time()
result1 = fib_slow(n)
slow_time = time.time() - start

start = time.time()
result2 = fib_memo(n)
fast_time = time.time() - start

print(f"\nfib({n}) = {result1}")
print(f"Without cache: {slow_time:.3f}s")
print(f"With cache:    {fast_time:.6f}s")
print(f"Speedup: {slow_time/fast_time:.0f}x faster!")