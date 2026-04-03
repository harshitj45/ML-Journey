def describe(data, name="Dataset"):
    """
    Complete statistical description.
    Mimics pandas df.describe()

    Args:
        data: list of numbers
        name: dataset name for display

    Returns:
        dict with all statistics
    """
    if not data:
        raise ValueError("Empty data!")

    n = len(data)
    sorted_data = sorted(data)

    # Mean
    mean = sum(data) / n

    # Variance + Std Dev
    variance = sum(
        (x - mean) ** 2
        for x in data
    ) / n
    std = variance ** 0.5

    # Median
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] +
                  sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    # Mode (most frequent)
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    mode = max(freq, key=freq.get)

    # Percentiles
    def percentile(sorted_d, p):
        idx = (p / 100) * (len(sorted_d) - 1)
        lower = int(idx)
        upper = lower + 1
        if upper >= len(sorted_d):
            return sorted_d[-1]
        frac = idx - lower
        return (sorted_d[lower] * (1 - frac) +
                sorted_d[upper] * frac)

    q1  = percentile(sorted_data, 25)
    q3  = percentile(sorted_data, 75)
    iqr = q3 - q1

    # Skewness (simplified)
    skewness = (
        3 * (mean - median) / std
        if std != 0 else 0
    )

    stats = {
        "count":    n,
        "mean":     round(mean, 4),
        "std":      round(std, 4),
        "min":      min(data),
        "25%":      round(q1, 4),
        "50%":      round(median, 4),
        "75%":      round(q3, 4),
        "max":      max(data),
        "mode":     mode,
        "variance": round(variance, 4),
        "iqr":      round(iqr, 4),
        "skewness": round(skewness, 4),
        "range":    max(data) - min(data),
    }

    # Print formatted output
    print(f"\n{'='*40}")
    print(f"  {name} — Statistical Summary")
    print(f"{'='*40}")
    print(f"  {'count':<12} {stats['count']:>10}")
    print(f"  {'mean':<12} {stats['mean']:>10.4f}")
    print(f"  {'std':<12} {stats['std']:>10.4f}")
    print(f"  {'min':<12} {stats['min']:>10}")
    print(f"  {'25%':<12} {stats['25%']:>10.4f}")
    print(f"  {'50% (med)':<12} {stats['50%']:>10.4f}")
    print(f"  {'75%':<12} {stats['75%']:>10.4f}")
    print(f"  {'max':<12} {stats['max']:>10}")
    print(f"  {'mode':<12} {stats['mode']:>10}")
    print(f"  {'variance':<12} {stats['variance']:>10.4f}")
    print(f"  {'iqr':<12} {stats['iqr']:>10.4f}")
    print(f"  {'skewness':<12} {stats['skewness']:>10.4f}")

    # Skewness interpretation
    if stats["skewness"] > 0.5:
        print(f"\n  ⚠ Positively skewed — "
              f"consider log transform")
    elif stats["skewness"] < -0.5:
        print(f"\n  ⚠ Negatively skewed")
    else:
        print(f"\n  ✓ Roughly symmetric")

    # Outlier detection using IQR
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers = [x for x in data
                if x < lower_fence
                or x > upper_fence]
    if outliers:
        print(f"  ⚠ Outliers detected: {outliers}")
    else:
        print(f"  ✓ No outliers detected")
    print(f"{'='*40}")

    return stats


# Test on different datasets:

# Dataset 1: Student marks
marks = [85, 92, 78, 95, 60,
         88, 72, 91, 65, 83,
         76, 89, 94, 70, 58]
describe(marks, "Student Marks")

# Dataset 2: Salary (with outlier)
salaries = [30000, 35000, 32000,
            38000, 31000, 29000,
            200000,  # outlier!
            33000, 36000, 34000]
describe(salaries, "Salaries")

# Dataset 3: Skewed data
import random
random.seed(42)
# Right-skewed: most values low,
# few very high
skewed = [random.randint(1, 10)
          for _ in range(20)] + \
         [random.randint(80, 100)
          for _ in range(3)]
describe(skewed, "Skewed Data")

