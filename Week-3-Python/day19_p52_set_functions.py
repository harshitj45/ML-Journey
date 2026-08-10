# ============================================
# Day 19 - Program 52
# Topic: Set Notation and Math Functions
# Concepts: set membership (in / not in),
#           issubset, function composition,
#           type hints
# ============================================


def is_member(element: str, group: set) -> bool:
    # I check if an element belongs to a set.
    return element in group


def is_not_member(element: str, group: set) -> bool:
    # I check if an element does not belong to a set.
    return element not in group


def check_subset(small: set, big: set) -> bool:
    # I check if the small set is a subset of the big set.
    return small.issubset(big)


def f(x: float) -> float:
    # I represent the math function f(x) = 2x + 3.
    return 2 * x + 3


def g(x: float) -> float:
    # I represent the math function g(x) = x squared.
    return x ** 2


def compose(x: float) -> float:
    # I calculate g(f(x)) — I apply f first, then g.
    return g(f(x))


# --- TESTING ---

train_features = {"age", "income", "score", "city"}
subset_features = {"age", "income"}

print(is_member("age", train_features))        # True
print(is_not_member("name", train_features))    # True
print(check_subset(subset_features, train_features))  # True

print(f(5))            # 13
print(g(4))             # 16
print(compose(5))       # g(f(5)) = g(13) = 169

empty_set = set()
print(len(empty_set) == 0)   # True


