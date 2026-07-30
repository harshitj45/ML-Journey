# ---------------- Base Class ---------------- #

class Person:
    """Base class for all people in the hospital."""

    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def display_details(self):
        print(f"ID   : {self.person_id}")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ---------------- Derived Class: Doctor ---------------- #

class Doctor(Person):

    def __init__(self, person_id, name, age, specialization, salary):
        # Call the constructor of the base class to initialize common attributes.
        super().__init__(person_id, name, age)
        self.specialization = specialization
        self.salary = salary

    def display_details(self):
        # Reuse the base class display method, then add doctor-specific details.
        super().display_details()
        print(f"Specialization : {self.specialization}")
        print(f"Salary         : ₹{self.salary}")

    def duty(self):
        print(f"Dr. {self.name} is treating patients.")


# ---------------- Derived Class: Patient ---------------- #

class Patient(Person):

    def __init__(self, person_id, name, age, disease, room_no):
        # Initialize shared person information first.
        super().__init__(person_id, name, age)
        self.disease = disease
        self.room_no = room_no

    def display_details(self):
        # Display common person information before patient-specific information.
        super().display_details()
        print(f"Disease : {self.disease}")
        print(f"Room No : {self.room_no}")

    def treatment(self):
        print(f"{self.name} is receiving treatment.")


# ---------------- Main Program ---------------- #

doctor = Doctor(
    person_id=101,
    name="Amit Sharma",
    age=45,
    specialization="Cardiologist",
    salary=120000
)

patient = Patient(
    person_id=201,
    name="Harshit Jain",
    age=22,
    disease="Viral Fever",
    room_no=205
)

print("=" * 40)
print("DOCTOR DETAILS")
print("=" * 40)
doctor.display_details()
doctor.duty()

print("\n" + "=" * 40)
print("PATIENT DETAILS")
print("=" * 40)
patient.display_details()
patient.treatment()





# ========================================
# DOCTOR DETAILS
# ========================================
# ID   : 101
# Name : Amit Sharma
# Age  : 45
# Specialization : Cardiologist
# Salary         : ₹120000
# Dr. Amit Sharma is treating patients.

# ========================================
# PATIENT DETAILS
# ========================================
# ID   : 201
# Name : Harshit Jain
# Age  : 22
# Disease : Viral Fever
# Room No : 205
# Harshit Jain is receiving treatment.