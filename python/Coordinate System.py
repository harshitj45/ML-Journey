import math

points = [(0,0), (3,4), (1,1), (6,8)]

# List to store distances
distances = []

# Calculate distance for each point
for (x, y) in points:
    d = math.sqrt(x**2 + y**2)
    distances.append(d)
    print(f"Point ({x},{y}) is {d:.2f} units away")

# Closest point
min_dist = min(distances)
min_index = distances.index(min_dist)

# Farthest point
max_dist = max(distances)
max_index = distances.index(max_dist)

print("\nClosest Point:", points[min_index])
print("Farthest Point:", points[max_index])