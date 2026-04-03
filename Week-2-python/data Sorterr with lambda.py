# Lambda + sorted() + map() + filter()


students = [
    {"name": "Harshit", "marks": 85,
     "age": 21, "city": "Delhi",   "dept": "CSE"},
    {"name": "Priya",   "marks": 92,
     "age": 20, "city": "Mumbai",  "dept": "ECE"},
    {"name": "Rahul",   "marks": 67,
     "age": 22, "city": "Chennai", "dept": "CSE"},
    {"name": "Neha",    "marks": 78,
     "age": 21, "city": "Delhi",   "dept": "ME"},
    {"name": "Arjun",   "marks": 45,
     "age": 23, "city": "Mumbai",  "dept": "CSE"},
    {"name": "Sneha",   "marks": 96,
     "age": 20, "city": "Delhi",   "dept": "ECE"},
    {"name": "Karan",   "marks": 55,
     "age": 22, "city": "Chennai", "dept": "CSE"},
]

print("=" * 50)
print("SORTING OPERATIONS")
print("=" * 50)

# Sort 1: By marks descending
by_marks = sorted(students,
                  key=lambda s: s["marks"],
                  reverse=True)
print("\n1. By Marks (High → Low):")
for s in by_marks:
    print(f"   {s['name']:<10} {s['marks']}")

# Sort 2: By name alphabetical
by_name = sorted(students,
                 key=lambda s: s["name"])
print("\n2. By Name (A → Z):")
for s in by_name:
    print(f"   {s['name']}")

# Sort 3: By city then marks
by_city_marks = sorted(
    students,
    key=lambda s: (s["city"], -s["marks"])
)
print("\n3. By City then Marks:")
for s in by_city_marks:
    print(f"   {s['city']:<10} "
          f"{s['name']:<10} {s['marks']}")

# Sort 4: By age then name
by_age_name = sorted(
    students,
    key=lambda s: (s["age"], s["name"])
)
print("\n4. By Age then Name:")
for s in by_age_name:
    print(f"   Age {s['age']}: {s['name']}")

print("\n" + "=" * 50)
print("FILTERING OPERATIONS")
print("=" * 50)

# Filter 1: Passed students
passed = list(filter(
    lambda s: s["marks"] >= 50, students
))
print(f"\n1. Passed ({len(passed)}):",
      [s["name"] for s in passed])

# Filter 2: CSE students
cse = list(filter(
    lambda s: s["dept"] == "CSE", students
))
print(f"2. CSE students ({len(cse)}):",
      [s["name"] for s in cse])

# Filter 3: Top performers
top = list(filter(
    lambda s: s["marks"] >= 80, students
))
print(f"3. Top performers (80+):",
      [s["name"] for s in top])

# Filter 4: Chained filters
delhi_cse_passed = list(filter(
    lambda s: (s["city"] == "Delhi" and
               s["dept"] == "CSE" and
               s["marks"] >= 50),
    students
))
print(f"4. Delhi CSE Passed:",
      [s["name"] for s in delhi_cse_passed])

print("\n" + "=" * 50)
print("MAPPING OPERATIONS")
print("=" * 50)

# Map 1: Add grade field
with_grade = list(map(
    lambda s: {**s,
               "grade": (
                   "A+" if s["marks"] >= 90 else
                   "A"  if s["marks"] >= 80 else
                   "B"  if s["marks"] >= 70 else
                   "C"  if s["marks"] >= 60 else
                   "F"
               )},
    students
))
print("\n1. With Grades:")
for s in with_grade:
    print(f"   {s['name']:<10} "
          f"{s['marks']} → {s['grade']}")

# Map 2: Extract only names + marks
name_marks = list(map(
    lambda s: (s["name"], s["marks"]),
    students
))
print("\n2. Name-Marks pairs:", name_marks)

# Map 3: Normalize marks 0-1
max_marks = max(s["marks"] for s in students)
min_marks = min(s["marks"] for s in students)

normalized = list(map(
    lambda s: {
        "name": s["name"],
        "normalized": round(
            (s["marks"] - min_marks) /
            (max_marks - min_marks), 3
        )
    },
    students
))
print("\n3. Normalized Marks:")
for s in normalized:
    print(f"   {s['name']:<10} "
          f"{s['normalized']:.3f}")

# Combined pipeline:
print("\n" + "=" * 50)
print("COMBINED PIPELINE")
print("=" * 50)

# Filter passed → Sort by marks →
# Map to show name + grade
result = sorted(
    filter(lambda s: s["marks"] >= 50,
           students),
    key=lambda s: s["marks"],
    reverse=True
)

print("\nPassed students ranked:")
for rank, s in enumerate(result, 1):
    grade = ("A+" if s["marks"] >= 90 else
             "A"  if s["marks"] >= 80 else
             "B"  if s["marks"] >= 70 else
             "C")
    print(f"  {rank}. {s['name']:<10} "
          f"{s['marks']} ({grade})")