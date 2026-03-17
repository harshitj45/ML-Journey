sentence = "Harshit is learning Machine Learning"

# Total characters (with spaces)
total_chars = len(sentence)

# Total words
words = sentence.split()
total_words = len(words)

# Uppercase version
upper_case = sentence.upper()

# First word and last word
first_word = words[0]
last_word = words[-1]

# Reverse sentence
reverse_sentence = sentence[::-1]

# Check "Machine" in sentence
check_machine = "Machine" in sentence

# Replace "Machine Learning" with "ML"
replace_text = sentence.replace("Machine Learning", "ML")

# Print all results
print("Sentence:", sentence)
print("Total characters:", total_chars)
print("Total words:", total_words)
print("Uppercase:", upper_case)
print("First word:", first_word)
print("Last word:", last_word)
print("Reverse sentence:", reverse_sentence)
print('Is "Machine" in sentence?:', check_machine)
print("After replacement:", replace_text)