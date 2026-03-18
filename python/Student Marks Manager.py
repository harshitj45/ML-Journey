marks = [85, 92, 78, 95, 60, 88, 72]

# Total marks
total = sum(marks)

# Average marks
average = total / len(marks)

# Highest mark and index
highest = max(marks)
highest_index = marks.index(highest)

# Lowest mark and index
lowest = min(marks)
lowest_index = marks.index(lowest)

# Marks above 80
above_80 = [m for m in marks if m > 80]

# Sorted marks
ascending = sorted(marks)
descending = sorted(marks, reverse=True)

# Add new mark
marks.append(91)

# Remove lowest mark
marks.remove(min(marks))

# Print results
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest, "at index", highest_index)
print("Lowest:", lowest, "at index", lowest_index)
print("Marks above 80:", above_80)
print("Ascending:", ascending)
print("Descending:", descending)
print("After adding 91:", marks)
print("After removing lowest:", marks)