# ============================================
# Day 15 - Program 42
# Topic: Batch Generator
# Concepts: yield, generator function,
#           list slicing (Day 3 se)
# Note: Yeh concept Deep Learning mein
#       data batches ke liye use hota hai
# ============================================


def batch_generator(data, batch_size):
    # data ko batch_size ke groups mein yield 
    start = 0
    while start < len(data):
        # slicing — Day 3 
        batch  = data[start : start + batch_size]
        yield batch                 # ek batch do
        start += batch_size         # agla batch


def read_lines(filename):
    # file ki lines ek ek yield karo
    # ek baar mein poori file load nahi hoti
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()  # ek line yield

    except FileNotFoundError:
        print(f"File nahi mili: {filename}")
        return


def number_generator(start, end, step=1):
    # range ki tarah — lekin generator hai
    current = start
    while current <= end:
        yield current
        current += step


# --- TESTING ---

# Batch generator:
data = [10, 20, 30, 40, 50,
        60, 70, 80, 90, 100]

print("Batches of size 3:")
for i, batch in enumerate(batch_generator(data, 3), 1):
    print(f"  Batch {i}: {batch}")
# Batch 1: [10, 20, 30]
# Batch 2: [40, 50, 60]
# Batch 3: [70, 80, 90]
# Batch 4: [100]

print("\nBatches of size 4:")
for i, batch in enumerate(batch_generator(data, 4), 1):
    print(f"  Batch {i}: {batch}")

# File ke liye — test file banao pehle:
with open("test_data.txt", "w") as f:
    f.write("Harshit,85\n")
    f.write("Priya,92\n")
    f.write("Rahul,67\n")
    f.write("Neha,78\n")

print("\nFile lines one by one:")
for line in read_lines("test_data.txt"):
    name, marks = line.split(",")
    print(f"  {name}: {marks}")

# Number generator:
print("\nNumbers 0-10 step 2:")
for n in number_generator(0, 10, 2):
    print(n, end=" ")       # 0 2 4 6 8 10
print()



