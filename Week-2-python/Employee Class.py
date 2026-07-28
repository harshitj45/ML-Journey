# ============================================
# PROGRAM 27: Employee Class
# CONCEPTS: class variable, instance variable,
#           methods, __str__, __gt__, __lt__,
#           sorted() with dunder methods
# ============================================

class Employee:

    company       = "ML Corp"
    total_emp     = 0          

    def __init__(self, name, salary, dept):
        self.name   = name
        self.salary = salary
        self.dept   = dept

        Employee.total_emp += 1

    def give_raise(self, amount):
        self.salary += amount
        return self             

    def details(self):
        print(f"Name: {self.name} | "
              f"Dept: {self.dept} | "
              f"Salary: Rs.{self.salary}")

    def __str__(self):
        return f"{self.name} ({self.dept}) - Rs.{self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary


# ── TESTS ──

e1 = Employee("Harshit", 50000, "ML")
e2 = Employee("Priya",   70000, "Data")
e3 = Employee("Rahul",   45000, "ML")

# Class variable:
print(f"Company: {Employee.company}")      
print(f"Total employees: {Employee.total_emp}")  

# Methods:
e1.details()    

# Method chaining:
e1.give_raise(5000).give_raise(3000)
e1.details()    

# Dunder comparison:
print(e1 > e3) 
print(e2 > e1)  
print(e1 == e3) 

employees = [e1, e2, e3]

print("\nSalary ascending:")
for e in sorted(employees):
    print(f"  {e}")

print("\nSalary descending:")
for e in sorted(employees, reverse=True):
    print(f"  {e}")
