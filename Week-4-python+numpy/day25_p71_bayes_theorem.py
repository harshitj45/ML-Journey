# ============================================
# Day 25 - Program 71
# Topic: Bayes Theorem Calculator
# Concepts: P(A|B) = P(B|A)*P(A)/P(B),
#           prior, likelihood, posterior
# ============================================


def calculate_evidence(p_b_given_a: float, p_a: float,
                        p_b_given_not_a: float, p_not_a: float) -> float:
    # I calculate the total probability of B happening,
    # by adding up both ways B could occur.
    return (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)


def bayes_theorem(p_b_given_a: float, p_a: float, p_b: float) -> float:
    # I calculate the posterior probability P(A given B)
    # using Bayes theorem.
    return (p_b_given_a * p_a) / p_b


def medical_test_analysis(prior_disease: float, sensitivity: float,
                           false_positive_rate: float) -> dict:
    # I analyze how reliable a positive test result actually is,
    # given how rare the disease is.
    prior_no_disease = 1 - prior_disease

    p_positive = calculate_evidence(
        sensitivity, prior_disease,
        false_positive_rate, prior_no_disease
    )

    p_disease_given_positive = bayes_theorem(
        sensitivity, prior_disease, p_positive
    )

    return {
        "p_positive_overall": p_positive,
        "p_disease_given_positive": p_disease_given_positive,
    }


def spam_word_analysis(prior_spam: float, likelihood_word_given_spam: float,
                        evidence_word: float) -> float:
    # I calculate how likely an email is spam, given that
    # it contains a specific word.
    return bayes_theorem(likelihood_word_given_spam, prior_spam, evidence_word)


# --- TESTING ---

result = medical_test_analysis(
    prior_disease=0.01,
    sensitivity=0.99,
    false_positive_rate=0.05
)
print(f"P(Positive test overall): {result['p_positive_overall']:.4f}")
print(f"P(Disease | Positive): {result['p_disease_given_positive']:.4f}")

# I test with a rarer disease to see how the result changes.
result_rare = medical_test_analysis(
    prior_disease=0.001,
    sensitivity=0.99,
    false_positive_rate=0.05
)
print(f"Rarer disease - P(Disease | Positive): {result_rare['p_disease_given_positive']:.4f}")

# I apply Bayes theorem to a spam-detection scenario.
posterior_spam = spam_word_analysis(
    prior_spam=0.3,
    likelihood_word_given_spam=0.6,
    evidence_word=0.25
)
print(f"P(Spam | contains 'win'): {posterior_spam:.4f}")
