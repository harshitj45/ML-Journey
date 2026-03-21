raw_data = [
    "Harshit,21,8.5,Delhi,CSE",
    "Priya,20,9.1,Mumbai,ECE",
    "Rahul,22,7.8,Chennai,CSE",
    "Neha,21,8.9,Delhi,ME",
    "Arjun,23,6.5,Mumbai,CSE",
    "Sneha,20,9.5,Delhi,CSE",
    "Karan,22,7.2,Chennai,ECE",
    "Meera,21,8.1,Mumbai,CSE",
]

headers = ["name", "age", "cgpa", "city", "dept"]

# Convert CSV rows → list of dictionaries
students = []
for row in raw_data:
    values = row.split(",")
    student = {}
    for i, header in enumerate(headers):
        value = values[i]
        if header == "age":
            student[header] = int(value)
        elif header == "cgpa":
            student[header] = float(value)
        else:
            student[header] = value
    students.append(student)

print(f"Loaded {len(students)} students\n")

# Print table format
print("=" * 55)
print(f"{'Name':<10} {'Age':>4} {'CGPA':>6} "
      f"{'City':<10} {'Dept':<5}")
print("-" * 55)

for s in students:
    print(f"{s['name']:<10} {s['age']:>4} "
          f"{s['cgpa']:>6.1f} "
          f"{s['city']:<10} {s['dept']:<5}")

print("=" * 55)

# Filter Delhi students
print("\nDelhi Students:")
for s in students:
    if s["city"] == "Delhi":
        print(f"  {s['name']}: {s['cgpa']}")

# Sort by CGPA (descending)
sorted_students = students.copy()
for i in range(1, len(sorted_students)):
    key = sorted_students[i]
    j = i - 1
    while j >= 0 and sorted_students[j]["cgpa"] < key["cgpa"]:
        sorted_students[j+1] = sorted_students[j]
        j -= 1
    sorted_students[j+1] = key

print("\nRankings by CGPA:")
for rank, s in enumerate(sorted_students, 1):
    medal = "🥇" if rank == 1 else \
            "🥈" if rank == 2 else \
            "🥉" if rank == 3 else f"{rank}."
    print(f"  {medal} {s['name']}: {s['cgpa']}")

# Department-wise statistics
print("\nDepartment Statistics:")
dept_data = {}

for s in students:
    dept = s["dept"]
    if dept not in dept_data:
        dept_data[dept] = []
    dept_data[dept].append(s["cgpa"])

for dept, cgpas in sorted(dept_data.items()):
    avg = sum(cgpas) / len(cgpas)
    best = max(cgpas)
    count = len(cgpas)
    print(f"  {dept}: count={count} avg={avg:.2f} best={best:.1f}")

# City-wise student list
print("\nCity Breakdown:")
city_students = {}

for s in students:
    city = s["city"]
    if city not in city_students:
        city_students[city] = []
    city_students[city].append(s["name"])

for city, names in sorted(city_students.items()):
    print(f"  {city} ({len(names)}): {', '.join(names)}")

# Find topper of each city
print("\nCity Toppers:")
city_topper = {}

for s in students:
    city = s["city"]
    if city not in city_topper:
        city_topper[city] = s
    elif s["cgpa"] > city_topper[city]["cgpa"]:
        city_topper[city] = s

for city, topper in sorted(city_topper.items()):
    print(f"  {city}: {topper['name']} ({topper['cgpa']})")

# Export as CSV format
print("\nCSV Export:")
print(",".join(headers + ["grade", "rank"]))

for rank, s in enumerate(sorted_students, 1):
    if s["cgpa"] >= 9.0:
        grade = "Outstanding"
    elif s["cgpa"] >= 8.0:
        grade = "Excellent"
    elif s["cgpa"] >= 7.0:
        grade = "Good"
    else:
        grade = "Average"

    row = [s["name"], str(s["age"]),
           str(s["cgpa"]), s["city"],
           s["dept"], grade, str(rank)]
    print(",".join(row))