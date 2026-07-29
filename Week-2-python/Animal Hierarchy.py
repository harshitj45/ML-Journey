# ============================================
# Day 11 - Program 28
# Topic: Animal Hierarchy
# Concepts: Inheritance, super(), override,
#           isinstance()
# ============================================


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"{self.name} eating")

    def sleep(self):
        print(f"{self.name} sleeping")

    def __str__(self):
        return f"{self.name} (age: {self.age})"


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)  
        self.breed = breed           

    # Override — Animal ka speak replace karo
    def speak(self):
        print(f"{self.name} says: Woof!")

    def __str__(self):
        # Override — apna format
        return f"Dog: {self.name} | {self.breed} | age:{self.age}"


class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)  
        self.color = color          

    # Override
    def speak(self):
        print(f"{self.name} says: Meow!")

    def __str__(self):
        return f"Cat: {self.name} | {self.color} | age:{self.age}"


# --- TESTING ---

d = Dog("Rex", 3, "Labrador")
c = Cat("Whiskers", 2, "White")

# Animal se mile methods:
d.eat()       # Rex eating
d.sleep()     # Rex sleeping
c.eat()       # Whiskers eating

# Override methods:
d.speak()     # Rex says: Woof!
c.speak()     # Whiskers says: Meow!

# __str__:
print(d)      # Dog: Rex | Labrador | age:3
print(c)      # Cat: Whiskers | White | age:2

# isinstance check:
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))  # True — Dog, Animal bhi hai
print(isinstance(d, Cat))     # False