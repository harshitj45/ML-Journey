# ============================================
# Day 25 - Program 72
# Topic: Naive Bayes Spam Classifier from Scratch
# Concepts: word frequency counting, Laplace smoothing,
#           multiplying probabilities, class comparison
# ============================================

from collections import Counter


def tokenize(text: str) -> list:
    # I split a message into lowercase words.
    return text.lower().split()


def build_word_counts(messages: list) -> Counter:
    # I count how many times each word appears
    # across all messages in one class.
    counts = Counter()
    for message in messages:
        counts.update(tokenize(message))
    return counts


def word_probability(word: str, word_counts: Counter,
                      total_words: int, vocab_size: int) -> float:
    # I calculate P(word | class) using Laplace smoothing,
    # so a word I never saw during training does not
    # give a probability of zero.
    count = word_counts.get(word, 0)
    return (count + 1) / (total_words + vocab_size)


def classify(message: str, spam_words: Counter, ham_words: Counter,
             p_spam: float, p_ham: float, vocab_size: int) -> str:
    # I compare the spam score and ham score for a new
    # message and return whichever class scores higher.
    words = tokenize(message)

    total_spam_words = sum(spam_words.values())
    total_ham_words = sum(ham_words.values())

    spam_score = p_spam
    ham_score = p_ham

    for word in words:
        spam_score *= word_probability(word, spam_words, total_spam_words, vocab_size)
        ham_score *= word_probability(word, ham_words, total_ham_words, vocab_size)

    return "SPAM" if spam_score > ham_score else "HAM"


# --- TESTING ---

spam_messages = [
    "win money now",
    "free prize click here",
    "make money fast",
    "win free cash now",
]

ham_messages = [
    "meeting at 3pm tomorrow",
    "project deadline next week",
    "please review the code",
    "team meeting scheduled",
]

spam_word_counts = build_word_counts(spam_messages)
ham_word_counts = build_word_counts(ham_messages)

all_words = set(spam_word_counts.keys()) | set(ham_word_counts.keys())
vocabulary_size = len(all_words)

total_messages = len(spam_messages) + len(ham_messages)
p_spam = len(spam_messages) / total_messages
p_ham = len(ham_messages) / total_messages

# I test the classifier on new, unseen messages.
test_messages = [
    "win free money now",
    "team project meeting tomorrow",
    "click here for free prize",
    "please schedule the review",
]

for message in test_messages:
    result = classify(message, spam_word_counts, ham_word_counts, p_spam, p_ham, vocabulary_size)
    print(f"'{message}' -> {result}")
