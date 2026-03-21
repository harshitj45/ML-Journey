numbers = [45, 72, 13, 89, 34,
           56, 91, 28, 67, 42,
           81, 15, 63, 37, 94]

print(f"Dataset: {numbers}")
print(f"Count: {len(numbers)}")

# Max manually
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Maximum: {max_val}")

# Min manually
min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num
print(f"Minimum: {min_val}")

# Sum + Average
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average:.2f}")

# Prime check function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Prime numbers in list
primes = []
for num in numbers:
    if is_prime(num):
        primes.append(num)
print(f"Prime numbers: {primes}")

# Pairs summing to 100
print("Pairs summing to 100:")
pairs_found = 0
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 100:
            print(f"{numbers[i]} + {numbers[j]} = 100")
            pairs_found += 1

if pairs_found == 0:
    print("No pairs found")

# Second largest (remove duplicates + sort)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

n = len(unique)
for i in range(n):
    for j in range(0, n-i-1):
        if unique[j] > unique[j+1]:
            unique[j], unique[j+1] = unique[j+1], unique[j]

second_largest = unique[-2]
print(f"Second largest: {second_largest}")

# Moving average
window = 3
print(f"\nMoving average (window={window}):")
for i in range(len(numbers) - window + 1):
    w = numbers[i:i+window]
    total = 0
    for x in w:
        total += x
    avg = total / window
    print(w, "→", round(avg, 1))

# Frequency count
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Most frequent
most_common = numbers[0]
for num in freq:
    if freq[num] > freq[most_common]:
        most_common = num

print(f"\nMost frequent: {most_common} ({freq[most_common]} times)")