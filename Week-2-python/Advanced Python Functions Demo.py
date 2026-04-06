students = []

# -------- BASIC FUNCTIONS --------
def add_student(name, marks, city="Unknown"):
    students.append({"name": name, "marks": marks, "city": city})

def display_students():
    for s in students:
        print(s["name"], s["marks"], s["city"])
    print()

# -------- RETURN MULTIPLE VALUES --------
def get_stats():
    if not students:
        return 0, 0, 0
    
    total = 0
    max_marks = students[0]["marks"]
    min_marks = students[0]["marks"]

    for s in students:
        m = s["marks"]
        total += m
        if m > max_marks:
            max_marks = m
        if m < min_marks:
            min_marks = m

    avg = total / len(students)
    return avg, max_marks, min_marks

# -------- DEFAULT + KEYWORD ARGUMENTS --------
def filter_students(min_marks=0, city=None):
    result = []
    for s in students:
        if s["marks"] >= min_marks:
            if city is None or s["city"] == city:
                result.append(s)
    return result

# -------- *ARGS --------
def add_many_students(*args):
    for data in args:
        name, marks, city = data
        add_student(name, marks, city)

# -------- **KWARGS --------
def update_student(name, **kwargs):
    for s in students:
        if s["name"] == name:
            for key in kwargs:
                s[key] = kwargs[key]

# -------- FUNCTION AS VARIABLE --------
def get_marks(student):
    return student["marks"]

def sort_students(key_func):
    data = students.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if key_func(data[j]) > key_func(data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data

# -------- LAMBDA FUNCTION --------
def sort_by_marks_lambda():
    return sort_students(lambda s: s["marks"])

# -------- HIGHER ORDER FUNCTION --------
def apply_operation(func):
    result = []
    for s in students:
        result.append(func(s))
    return result

# -------- NESTED FUNCTION --------
def grade_system():
    def get_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"

    grades = {}
    for s in students:
        grades[s["name"]] = get_grade(s["marks"])
    return grades

# -------- RECURSION --------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# -------- SEARCH FUNCTION --------
def search_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None

# -------- DELETE FUNCTION --------
def delete_student(name):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            return True
    return False

# -------- MAIN EXECUTION --------
def main():
    # add using normal function
    add_student("Harshit", 85, "Delhi")
    add_student("Priya", 92, "Mumbai")

    # add using *args
    add_many_students(
        ("Rahul", 70, "Chennai"),
        ("Neha", 88, "Delhi"),
        ("Arjun", 60, "Mumbai")
    )

    print("All Students:")
    display_students()

    # stats
    avg, max_m, min_m = get_stats()
    print("Average:", avg, "Max:", max_m, "Min:", min_m)

    # filter
    print("\nFiltered (marks >= 80):")
    print(filter_students(min_marks=80))

    # update using kwargs
    update_student("Rahul", marks=75, city="Delhi")

    # sorting
    print("\nSorted by marks:")
    sorted_data = sort_by_marks_lambda()
    for s in sorted_data:
        print(s)

    # higher order function
    print("\nMarks list:")
    print(apply_operation(get_marks))

    # nested function (grades)
    print("\nGrades:")
    print(grade_system())

    # recursion
    print("\nFactorial of 5:", factorial(5))

    # search
    print("\nSearch Priya:")
    print(search_student("Priya"))

    # delete
    print("\nDeleting Arjun:", delete_student("Arjun"))

    print("\nFinal Data:")
    display_students()

# -------- START --------
main()