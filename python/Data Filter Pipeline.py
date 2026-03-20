students = [
    {"name": "Harshit", "marks": 85, "city": "Delhi", "dept": "CSE"},
    {"name": "Priya", "marks": 45, "city": "Mumbai", "dept": "ECE"},
    {"name": "Rahul", "marks": 92, "city": "Delhi", "dept": "CSE"},
    {"name": "Neha", "marks": 67, "city": "Chennai", "dept": "CSE"},
    {"name": "Arjun", "marks": 38, "city": "Delhi", "dept": "ME"},
    {"name": "Sneha", "marks": 78, "city": "Mumbai", "dept": "CSE"},
    {"name": "Karan", "marks": 55, "city": "Delhi", "dept": "ECE"}
]

# Passed students
passed = []
for s in students:
    if s["marks"] >= 50:
        passed.append(s["name"])
print("Passed:", passed)

# Delhi marks
delhi_marks = []
for s in students:
    if s["city"] == "Delhi":
        delhi_marks.append(s["marks"])
print("Delhi marks:", delhi_marks)

# Name - Marks
name_marks = {}
for s in students:
    name_marks[s["name"]] = s["marks"]
print("Name-Marks:", name_marks)

# Grade function
def get_grade(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    elif m >= 50:
        return "D"
    else:
        return "F"

# Name - Grade
name_grade = {}
for s in students:
    name_grade[s["name"]] = get_grade(s["marks"])
print("Grades:", name_grade)

# Failed Delhi students
failed_delhi = []
for s in students:
    if s["city"] == "Delhi" and s["marks"] < 50:
        failed_delhi.append(s["name"])
print("Failed in Delhi:", failed_delhi)

# Unique cities
cities = []
for s in students:
    if s["city"] not in cities:
        cities.append(s["city"])
print("Cities:", cities)

# CSE passed students
cse_passed = []
for s in students:
    if s["dept"] == "CSE" and s["marks"] >= 50:
        cse_passed.append(s["name"])
print("CSE Passed:", cse_passed)

# Average marks per city
city_marks = {}

for s in students:
    city = s["city"]
    if city not in city_marks:
        city_marks[city] = []
    city_marks[city].append(s["marks"])

print("\nCity-wise average:")
for city in city_marks:
    marks = city_marks[city]
    avg = sum(marks) / len(marks)
    print(city, ":", round(avg, 1))