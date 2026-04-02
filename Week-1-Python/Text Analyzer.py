import string

text = """
Machine learning is a subset of artificial intelligence.
Machine learning algorithms learn from data automatically.
Data is the fuel of machine learning systems.
Python is the most popular language for machine learning.
Deep learning is a subset of machine learning.
"""

# -------- PREPROCESSING --------

# Lowercase
text = text.lower()

# Remove punctuation
for ch in string.punctuation:
    text = text.replace(ch, "")

# Split into words
words = text.split()

print("Total words:", len(words))

# Unique words
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("Unique words:", len(unique_words))

# -------- ANALYSIS --------

# Word frequency
word_freq = {}

for w in words:
    if w in word_freq:
        word_freq[w] += 1
    else:
        word_freq[w] = 1

# Top 10 words (simple sorting)
sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)

print("\nTop words:")
count = 0
for w in sorted_words:
    print(w, ":", word_freq[w])
    count += 1
    if count == 10:
        break

# Words appearing once
print("\nWords appearing once:")
for w in word_freq:
    if word_freq[w] == 1:
        print(w)

# Word lengths
word_lengths = {}
for w in unique_words:
    word_lengths[w] = len(w)

# Long words (>6)
print("\nLong words (>6 letters):")
for w in unique_words:
    if len(w) > 6:
        print(w)

# Sentence analysis
sentences = text.split(".")

clean_sentences = []
for s in sentences:
    s = s.strip()
    if s != "":
        clean_sentences.append(s)

print("\nTotal sentences:", len(clean_sentences))

print("Words per sentence:")
i = 1
for s in clean_sentences:
    count = len(s.split())
    print("Sentence", i, ":", count)
    i += 1

# Bigram ("machine learning")
bigrams = []

for i in range(len(words) - 1):
    pair = words[i] + " " + words[i+1]
    bigrams.append(pair)

ml_count = 0
for b in bigrams:
    if b == "machine learning":
        ml_count += 1

print("\n'machine learning' appears:", ml_count, "times")

# TF Score
print("\nTF Scores:")
for w in word_freq:
    tf = word_freq[w] / len(words)
    print(w, ":", round(tf, 4))