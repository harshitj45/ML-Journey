# ============================================
# Day 17 - Program 46 (Main File)
# Topic: Importing a Custom Module
# Concepts: import, from-import, aliasing
# ============================================

# I import the whole module and use dot notation.
import calc_utils

# I also import specific functions directly.
from calc_utils import add, average

# I import with an alias for a shorter name.
import calc_utils as calc


# --- TESTING ---

# Using the full module name:
print(calc_utils.add(10, 5))
print(calc_utils.multiply(4, 6))

# Using directly imported functions:
print(add(20, 8))
print(average([85, 92, 67, 78]))

# Using the alias:
print(calc.subtract(50, 15))
print(calc.divide(10, 0))

marks = [85, 45, 92, 38, 78]
print(f"Average marks: {calc_utils.average(marks):.2f}")


