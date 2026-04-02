dataset1 = [1,2,3,4,5,6,7,8]
dataset2 = [5,6,7,8,9,10,11,12]

# Convert to sets
set1 = set(dataset1)
set2 = set(dataset2)

# Common elements (intersection)
common = set1 & set2

# Only in dataset1
only1 = set1 - set2

# Only in dataset2
only2 = set2 - set1

# All unique elements (union)
all_unique = set1 | set2

# In one but not both (symmetric difference)
sym_diff = set1 ^ set2

# Remove duplicates from combined list
combined = dataset1 + dataset2
no_duplicates = list(set(combined))

# Print results
print("Common elements:", common)
print("Only in dataset1:", only1)
print("Only in dataset2:", only2)
print("All unique (union):", all_unique)
print("Symmetric difference:", sym_diff)
print("Without duplicates:", no_duplicates)