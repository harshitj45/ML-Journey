# ============================================
# Day 11 - Program 30
# Topic: Shape → Circle, Rectangle, Triangle
# Concepts: Inheritance, super(), override,
#           sorted() with __lt__
# ============================================


class Shape:

    def __init__(self, color, name):
        self.color = color
        self.name  = name

    def describe(self):
        print(f"Shape : {self.name}")
        print(f"Color : {self.color}")

    def area(self):
        return 0

    def __str__(self):
        return f"{self.name} ({self.color}) area={self.area():.2f}"

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color, "Circle")  # parent ka init
        self.radius = radius

    def area(self):
        # Override — circle ka area
        return 3.14 * self.radius ** 2

    def describe(self):
        super().describe()                 # parent ka describe
        print(f"Radius: {self.radius}")
        print(f"Area  : {self.area():.2f}")


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color, "Rectangle")
        self.length = length
        self.width  = width

    def area(self):
        # Override — rectangle ka area
        return self.length * self.width

    def describe(self):
        super().describe()
        print(f"Length: {self.length}")
        print(f"Width : {self.width}")
        print(f"Area  : {self.area():.2f}")


class Triangle(Shape):

    def __init__(self, color, base, height):
        super().__init__(color, "Triangle")
        self.base   = base
        self.height = height

    def area(self):
        # Override — triangle ka area
        return 0.5 * self.base * self.height

    def describe(self):
        super().describe()
        print(f"Base  : {self.base}")
        print(f"Height: {self.height}")
        print(f"Area  : {self.area():.2f}")


# --- TESTING ---

c = Circle("Red", 7)
r = Rectangle("Blue", 5, 4)
t = Triangle("Green", 6, 8)

# describe() — super() + apna:
print("--- Circle ---")
c.describe()

print("\n--- Rectangle ---")
r.describe()

print("\n--- Triangle ---")
t.describe()

# __str__:
print(f"\n{c}")
print(f"{r}")
print(f"{t}")

# Comparison:
print(f"\nCircle > Rectangle: {c > r}")

# sorted() — __lt__ use hota hai automatically:
shapes = [c, r, t]
print("\nArea se ascending:")
for s in sorted(shapes):
    print(f"  {s}")

print("\nArea se descending:")
for s in sorted(shapes, reverse=True):
    print(f"  {s}")