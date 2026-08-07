# ============================================
# Day 17 - Program 48 (Main File)
# Topic: Importing a Module That Has a main Guard
# Concepts: import behavior with __name__ guard
# ============================================

import string_helper


# --- TESTING ---

# I print __name__ here to compare it with what
# string_helper.py prints when run directly.
print("This file's __name__ is:", __name__)

# The test block inside string_helper.py did NOT run
# just now, because I imported it instead of running
# string_helper.py directly. I only get its functions.

text = "I am learning Python modules"

print(string_helper.count_words(text))
print(string_helper.count_vowels(text))
print(string_helper.reverse_words(text))



