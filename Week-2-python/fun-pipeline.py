from functools import reduce

# ─────────────────────────────────
# ML Data Preprocessing Pipeline
# Using map + filter + reduce
# ─────────────────────────────────

raw_data = [
    None, 23, -5, 45, None,
    67, 200, 12, None, 89,
    -3, 34, 150, 56, None
]

print("Original data:", raw_data)
print(f"Length: {len(raw_data)}")

# Step 1: Remove None values
step1 = list(filter(
    lambda x: x is not None,
    raw_data
))
print(f"\nStep 1 — Remove None: {step1}")
print(f"Removed: {len(raw_data)-len(step1)} nulls")

# Step 2: Remove negatives
step2 = list(filter(
    lambda x: x > 0,
    step1
))
print(f"\nStep 2 — Remove negatives: {step2}")

# Step 3: Remove outliers (IQR method)
def remove_outliers(data):
    sorted_d = sorted(data)
    n = len(sorted_d)
    q1 = sorted_d[n//4]
    q3 = sorted_d[3*n//4]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [x for x in data
            if lower <= x <= upper]

step3 = remove_outliers(step2)
print(f"\nStep 3 — Remove outliers: {step3}")
print(f"Outliers removed: "
      f"{set(step2) - set(step3)}")

# Step 4: Normalize 0-1
min_val = reduce(lambda a,b: a if a<b else b,
                 step3)
max_val = reduce(lambda a,b: a if a>b else b,
                 step3)

step4 = list(map(
    lambda x: round(
        (x - min_val)/(max_val - min_val), 3
    ),
    step3
))
print(f"\nStep 4 — Normalize (0-1): {step4}")

# Step 5: Statistics on clean data
total   = reduce(lambda a,b: a+b, step4)
mean    = total / len(step4)
sq_diff = reduce(
    lambda a,b: a+b,
    map(lambda x: (x-mean)**2, step4)
)
std = (sq_diff / len(step4)) ** 0.5

print(f"\nFinal Stats:")
print(f"  Count : {len(step4)}")
print(f"  Mean  : {mean:.3f}")
print(f"  Std   : {std:.3f}")
print(f"  Min   : {min(step4)}")
print(f"  Max   : {max(step4)}")

# ─────────────────────────────────
# Pipeline as functions list
# ─────────────────────────────────
print("\n" + "="*40)
print("PIPELINE AS FUNCTION LIST")
print("="*40)

# Define pipeline steps as functions:
pipeline = [
    ("Remove None",
     lambda data: [x for x in data
                   if x is not None]),
    ("Remove negatives",
     lambda data: [x for x in data
                   if x > 0]),
    ("Remove outliers",
     remove_outliers),
    ("Normalize",
     lambda data: [
         round((x-min(data)) /
               (max(data)-min(data)), 3)
         for x in data
     ]),
]

# Run pipeline:
result = raw_data
for step_name, step_func in pipeline:
    prev_len = len([x for x in result
                    if x is not None])
    result = step_func(result)
    print(f"\n{step_name}:")
    print(f"  {result}")

print(f"\nFinal clean data ({len(result)} items):")
print(f"  {result}")

