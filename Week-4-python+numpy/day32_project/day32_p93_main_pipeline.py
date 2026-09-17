# ============================================
# Day 32 - Program 93 (Main)
# Topic: Week 4 Capstone — Full Data Pipeline
# Concepts: combining every array skill from
#           Days 22-31 into one realistic workflow
# ============================================

import numpy as np
from data_sources import combine_all_sources, add_student_ids
from data_cleaner import full_clean, label_performance


def print_pipeline_report(raw: np.ndarray, cleaned: np.ndarray) -> None:
    # I print a summary of what changed during cleaning.
    print("Data Pipeline Report")
    print(f"  Raw rows: {raw.shape[0]}")
    print(f"  Cleaned rows: {cleaned.shape[0]}")
    print(f"  Rows removed: {raw.shape[0] - cleaned.shape[0]}")


def train_test_split_manual(dataset: np.ndarray, train_ratio: float = 0.75) -> tuple:
    # I split the cleaned dataset into train and test sets.
    split_index = int(len(dataset) * train_ratio)
    train, test = np.split(dataset, [split_index])
    return train, test


def demonstrate_safe_editing(dataset: np.ndarray) -> None:
    # I show that editing a filtered subset never touches
    # the original cleaned dataset, because boolean
    # indexing always returns a copy (Day 31).
    high_performers = dataset[dataset[:, -1] >= 75]
    high_performers[0, 0] = -1
    print(f"Original dataset untouched: {dataset[0, 0] != -1}")


# --- RUN PIPELINE ---

with_ids = add_student_ids(combine_all_sources())
print(f"Combined raw dataset:\n{with_ids}")

# I clean using columns: id=0, hours=1, attendance=2, marks=3
cleaned = full_clean(with_ids, hours_col=1, marks_col=3)
print(f"\nCleaned + reordered dataset:\n{cleaned}")

print_pipeline_report(with_ids, cleaned)

labels = label_performance(cleaned, marks_col=3)
print(f"\nPerformance labels: {labels}")

train, test = train_test_split_manual(cleaned, train_ratio=0.75)
print(f"\nTrain shape: {train.shape}, Test shape: {test.shape}")

demonstrate_safe_editing(cleaned)

