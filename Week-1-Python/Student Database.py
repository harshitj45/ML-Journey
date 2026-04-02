# Student data (list of dictionaries)
students = [
    {"name": "Harshit", "age": 21, "marks": [85, 90, 78, 92, 88], "city": "Delhi"},
    {"name": "Aman", "age": 22, "marks": [70, 75, 68, 72, 74], "city": "Mumbai"},
    {"name": "Riya", "age": 20, "marks": [95, 98, 92, 96, 94], "city": "Pune"}
]

# Function: average
def get_average(student):
    return sum(student["marks"]) / len(student["marks"])

# Function: grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Function: print report
def print_report(student):
    avg = get_average(student)
    grade = get_grade(avg)
    
    print("="*25)
    print("Name :", student["name"])
    print("Age  :", student["age"])
    print("City :", student["city"])
    print("Marks:", student["marks"])
    print(f"Average: {avg:.2f}")
    print("Grade :", grade)

# Print report for all students
for s in students:
    print_report(s)

# Find student with highest average
top_student = students[0]
top_avg = get_average(top_student)

for s in students:
    avg = get_average(s)
    if avg > top_avg:
        top_avg = avg
        top_student = s

print("\nTop Student:", top_student["name"], "with avg", round(top_avg,2))