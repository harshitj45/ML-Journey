# --------- DATA ----------
students = []

# --------- FUNCTIONS ----------

# Add student
def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    city = input("Enter city: ")

    student = {"name": name, "marks": marks, "city": city}
    students.append(student)
    print("Student added!\n")

# Display students
def display_students():
    if len(students) == 0:
        print("No students found\n")
        return
    
    print("\nAll Students:")
    for s in students:
        print(s["name"], s["marks"], s["city"])
    print()

# Calculate average
def calculate_average():
    if len(students) == 0:
        return 0
    
    total = 0
    for s in students:
        total += s["marks"]
    
    return total / len(students)

# Find topper
def find_topper():
    if len(students) == 0:
        return None
    
    top = students[0]
    for s in students:
        if s["marks"] > top["marks"]:
            top = s
    return top

# Search student
def search_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None

# Delete student
def delete_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Deleted successfully\n")
            return
    print("Student not found\n")

# Grade function
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

# Show grades
def show_grades():
    if len(students) == 0:
        print("No data\n")
        return
    
    print("\nGrades:")
    for s in students:
        grade = get_grade(s["marks"])
        print(s["name"], "→", grade)
    print()

# Students above average
def above_average():
    avg = calculate_average()
    print("Average:", round(avg, 2))
    
    print("Above average students:")
    for s in students:
        if s["marks"] > avg:
            print(s["name"], s["marks"])
    print()

# --------- MENU ----------
def menu():
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Average Marks")
        print("4. Find Topper")
        print("5. Search Student")
        print("6. Delete Student")
        print("7. Show Grades")
        print("8. Above Average")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            avg = calculate_average()
            print("Average:", round(avg, 2), "\n")

        elif choice == "4":
            top = find_topper()
            if top:
                print("Topper:", top["name"], top["marks"], "\n")
            else:
                print("No data\n")

        elif choice == "5":
            name = input("Enter name to search: ")
            result = search_student(name)
            if result:
                print(result, "\n")
            else:
                print("Not found\n")

        elif choice == "6":
            name = input("Enter name to delete: ")
            delete_student(name)

        elif choice == "7":
            show_grades()

        elif choice == "8":
            above_average()

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice\n")

# --------- START ----------
menu()