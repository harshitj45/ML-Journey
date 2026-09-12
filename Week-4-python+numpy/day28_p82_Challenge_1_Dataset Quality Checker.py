# ============================================
# Day 29 - Program 82
# Topic: Dataset Quality Checker (Synthesis)
# Concepts: OOP, custom exceptions, file I/O,
#           NumPy stats, z-score outlier detection
# ============================================

import numpy as np


class DataLoadError(Exception):
    pass


class DatasetValidator:

    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

    def load_data(self):
        # I read the file, one number per line.
        try:
            with open(self.filename, "r") as f:
                values = [float(line.strip()) for line in f if line.strip()]
            self.data = np.array(values)
        except FileNotFoundError:
            raise DataLoadError(f"I could not find the file: {self.filename}")
        return self

    def get_stats(self) -> dict:
        return {
            "mean": np.mean(self.data),
            "std": np.std(self.data, ddof=1),
            "count": len(self.data),
        }

    def find_outliers(self, threshold: float = 2.0) -> np.ndarray:
        mean = np.mean(self.data)
        std = np.std(self.data)
        z_scores = (self.data - mean) / std
        return self.data[np.abs(z_scores) > threshold]

    def save_report(self, output_file: str):
        stats = self.get_stats()
        outliers = self.find_outliers()
        with open(output_file, "w") as f:
            f.write(f"Count: {stats['count']}\n")
            f.write(f"Mean: {stats['mean']:.4f}\n")
            f.write(f"Std: {stats['std']:.4f}\n")
            f.write(f"Outliers: {list(outliers)}\n")


# --- TESTING ---
with open("test_data.txt", "w") as f:
    for v in [85, 88, 90, 87, 86, 89, 91, 150, 84]:
        f.write(f"{v}\n")

validator = DatasetValidator("test_data.txt")
validator.load_data()
print(validator.get_stats())
print(validator.find_outliers())
validator.save_report("report.txt")

