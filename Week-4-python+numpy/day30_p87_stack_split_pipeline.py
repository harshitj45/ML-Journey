# ============================================
# Day 30 - Program 87
# Topic: Stacking Multiple Sources and Splitting Data
# Concepts: vstack, hstack, concatenate,
#           hsplit, vsplit, manual train/test split
# ============================================

import numpy as np


def combine_sources(sources: list) -> np.ndarray:
    # I stack multiple small datasets into one combined
    # dataset, the way I would when data comes from
    # several files or classes.
    return np.vstack(sources)


def add_feature_column(dataset: np.ndarray, new_column: np.ndarray) -> np.ndarray:
    # I add a new feature column to an existing dataset
    # using horizontal stacking.
    new_column = new_column.reshape(-1, 1)
    return np.hstack([dataset, new_column])


def split_features_and_labels(dataset: np.ndarray, label_col: int = -1) -> tuple:
    # I split a dataset into features and labels using hsplit.
    features = dataset[:, :label_col]
    labels = dataset[:, label_col]
    return features, labels


def manual_train_test_split(dataset: np.ndarray, train_ratio: float = 0.8) -> tuple:
    # I split a dataset into train and test sets using
    # np.split at a calculated index.
    split_index = int(len(dataset) * train_ratio)
    train, test = np.split(dataset, [split_index])
    return train, test


# --- TESTING ---

class_a = np.array([[85, 90], [78, 82]])
class_b = np.array([[92, 88], [70, 75]])
class_c = np.array([[60, 65], [55, 58]])

all_students = combine_sources([class_a, class_b, class_c])
print(f"Combined dataset shape: {all_students.shape}")
print(all_students)

attendance = np.array([95, 88, 92, 80, 75, 60])
with_attendance = add_feature_column(all_students, attendance)
print(f"\nWith attendance column:\n{with_attendance}")

features, labels = split_features_and_labels(with_attendance, label_col=-1)
print(f"\nFeatures:\n{features}")
print(f"Labels: {labels}")

train_set, test_set = manual_train_test_split(with_attendance, train_ratio=0.7)
print(f"\nTrain shape: {train_set.shape}")
print(f"Test shape: {test_set.shape}")

