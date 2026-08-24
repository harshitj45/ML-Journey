# ============================================
# Day 25 - Program 70
# Topic: Basic Probability Calculator
# Concepts: P(A), union, conditional probability,
#           independence check
# ============================================


def probability(favorable: int, total: int) -> float:
    # I calculate the basic probability of an event.
    return favorable / total


def complement(p_a: float) -> float:
    # I calculate the probability of an event NOT happening.
    return 1 - p_a


def union_probability(p_a: float, p_b: float, p_a_and_b: float) -> float:
    # I calculate P(A or B) using the inclusion-exclusion rule.
    # I subtract the overlap so it isn't counted twice.
    return p_a + p_b - p_a_and_b


def conditional_probability(p_a_and_b: float, p_b: float) -> float:
    # I calculate P(A given B) — the probability of A,
    # knowing that B has already happened.
    return p_a_and_b / p_b


def are_independent(p_a: float, p_b: float, p_a_and_b: float) -> bool:
    # I check independence by comparing the actual joint
    # probability with what it would be if A and B were independent.
    expected = p_a * p_b
    return abs(expected - p_a_and_b) < 0.001


# --- TESTING ---

# I roll a die: P(even number)
p_even = probability(3, 6)
print(f"P(even): {p_even}")
print(f"P(not even): {complement(p_even)}")

# I check P(King or Heart) from a deck of cards.
p_king = 4 / 52
p_heart = 13 / 52
p_king_and_heart = 1 / 52

p_king_or_heart = union_probability(p_king, p_heart, p_king_and_heart)
print(f"P(King or Heart): {p_king_or_heart:.4f}")

# I calculate a conditional probability.
p_submit_and_pass = 0.45
p_submit = 0.60
p_pass_given_submit = conditional_probability(p_submit_and_pass, p_submit)
print(f"P(Pass | Submitted): {p_pass_given_submit}")

# I check independence between two events.
p_rain = 0.3
p_traffic = 0.4
p_both = 0.25
print(are_independent(p_rain, p_traffic, p_both))

# I check two genuinely independent events (two coin flips).
p_heads_1 = 0.5
p_heads_2 = 0.5
p_both_heads = 0.25
print(are_independent(p_heads_1, p_heads_2, p_both_heads))

