# ============================================
# Day 11 - Program 29
# Topic: Employee → Manager
# Concepts: Inheritance, super().__init__,
#           super().method(), method override
# ============================================


class Employee:

    company = "ML Corp"         # class variable

    def __init__(self, name, salary, dept):
        self.name   = name
        self.salary = salary
        self.dept   = dept

    def give_raise(self, amount):
        self.salary += amount
        return self             # chaining

    def details(self):
        print(f"Name   : {self.name}")
        print(f"Dept   : {self.dept}")
        print(f"Salary : Rs.{self.salary}")

    def __str__(self):
        return f"{self.name} | {self.dept} | Rs.{self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary


class Manager(Employee):

    def __init__(self, name, salary, dept, team_size):
        super().__init__(name, salary, dept)
        # Apna extra variable:
        self.team_size = team_size
        self.team      = []         # team members list

    def add_member(self, employee):
        self.team.append(employee)

    def details(self):
        super().details()           # Employee ka details
        print(f"Team   : {self.team_size} members")

    def show_team(self):
        print(f"\n{self.name} ki team:")
        for emp in self.team:
            print(f"  {emp}")

    def __str__(self):
        return (f"{self.name} (Manager) | "
                f"{self.dept} | Rs.{self.salary}")


# --- TESTING ---

e1 = Employee("Harshit", 50000, "ML")
e2 = Employee("Rahul",   45000, "ML")
m  = Manager("Priya", 90000, "ML", 2)

# Employee methods:
e1.details()
print()

# Manager methods — super() se Employee bhi:
m.details()

# Team banao:
m.add_member(e1)
m.add_member(e2)
m.show_team()

# Raise:
e1.give_raise(5000)
print(f"\nAfter raise: {e1}")

# Comparison:
print(m > e1)     # True  (90000 > 55000)

# isinstance:
print(isinstance(m, Manager))   # True
print(isinstance(m, Employee))  # True — Manager, Employee bhi hai!