paragraph = """
Machine learning is a subset of 
artificial intelligence. Machine learning
algorithms learn from data. Data is the
fuel of machine learning.
"""

# Step 1: lowercase
text = paragraph.lower()

# Step 2: remove dot and newline
text = text.replace(".", "")
text = text.replace("\n", " ")

# Step 3: split into words
words = text.split()

# Step 4: count frequency
freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

# Step 5: print all frequencies
print("Word Frequencies:")
for word in freq:
    print(word, ":", freq[word])

# Step 6: words with count = 1
print("\nWords appearing only once:")
for word in freq:
    if freq[word] == 1:
        print(word)