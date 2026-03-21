n = 5

# Pattern 1: Right Triangle
print("Pattern 1 — Right Triangle:")
for i in range(1, n+1):
    print("*" * i)

# Pattern 2: Number Pyramid
print("\nPattern 2 — Number Pyramid:")
for i in range(1, n+1):
    spaces = " " * (n - i)
    nums = ""
    
    # Increasing numbers
    for j in range(1, i+1):
        nums += str(j)
    
    # Decreasing numbers
    for j in range(i-1, 0, -1):
        nums += str(j)
    
    print(spaces + nums)

# Pattern 3: Diamond
print("\nPattern 3 — Diamond:")

# Upper half
for i in range(1, n+1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Lower half
for i in range(n-1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Pattern 4: Multiplication Table
print("\nPattern 4 — Multiplication Table:")

# Header row
print("   ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()

print("   " + "-"*20)

# Table body
for i in range(1, 6):
    print(f"{i:2} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()