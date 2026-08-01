# ============================================
# Day 12 - Program 31
# Topic: Abstract Shape Class
# Concepts: ABC, @abstractmethod,
#           super().__init__, isinstance()
# ============================================

from abc import ABC, abstractmethod


class Shape(ABC):
    # Abstract class 

    def __init__(self, color):
        self.color = color          # common variable sabke liye

    @abstractmethod
    def area(self):
        pass                        # child ZAROOR implement kare

    @abstractmethod
    def perimeter(self):
        pass                        # child ZAROOR implement kare

    def describe(self):
        # Normal method — child ko override karna zaroor nahi
        print(f"Shape : {self.__class__.__name__}")
        print(f"Color : {self.color}")
        print(f"Area  : {self.area():.2f}")
        print(f"Peri  : {self.perimeter():.2f}")


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)     # parent ka color set
        self.radius = radius

    def area(self):                 # abstractmethod implement kiya
        return 3.14 * self.radius ** 2

    def perimeter(self):            # abstractmethod implement kiya
        return 2 * 3.14 * self.radius


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)     # parent ka color set
        self.length = length
        self.width  = width

    def area(self):                 # abstractmethod implement kiya
        return self.length * self.width

    def perimeter(self):            # abstractmethod implement kiya
        return 2 * (self.length + self.width)


class Triangle(Shape):

    def __init__(self, color, base, height, side):
        super().__init__(color)
        self.base   = base
        self.height = height
        self.side   = side          # equal sides assume

    def area(self):                 # abstractmethod implement kiya
        return 0.5 * self.base * self.height

    def perimeter(self):            # abstractmethod implement kiya
        return self.base + (2 * self.side)


# --- TESTING ---

# s = Shape("Red")   # Error — abstract class!

c = Circle("Red", 7)
r = Rectangle("Blue", 5, 4)
t = Triangle("Green", 6, 8, 5)

print("--- Circle ---")
c.describe()

print("\n--- Rectangle ---")
r.describe()

print("\n--- Triangle ---")
t.describe()

# isinstance — sab Shape ke objects hain
print(isinstance(c, Shape))      # True
print(isinstance(r, Shape))      # True
print(isinstance(t, Shape))      # True

# List mein rakh ke loop chalao
shapes = [c, r, t]
print("\nSab shapes ki area:")
for s in shapes:
    print(f"  {s.__class__.__name__}: {s.area():.2f}")