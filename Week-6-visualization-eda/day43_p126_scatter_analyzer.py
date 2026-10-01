# ============================================
# Day 43 - Program 126
# Topic: Scatter Plots with Color/Size Encoding
# Concepts: basic scatter, c= for color, s= for
#           size, colorbar, encoding extra dimensions
# ============================================

import matplotlib.pyplot as plt
import numpy as np


def plot_basic_scatter(x: np.ndarray, y: np.ndarray, xlabel: str, ylabel: str, filename: str) -> None:
    # I plot a basic scatter to see the relationship between
    # two numeric variables.
    plt.figure()
    plt.scatter(x, y, color="darkblue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"{xlabel} vs {ylabel}")
    plt.savefig(filename)
    plt.close()


def plot_scatter_with_color(x: np.ndarray, y: np.ndarray, color_values: np.ndarray,
                             color_label: str, filename: str) -> None:
    # I encode a third variable as color, so the plot shows
    # three dimensions of information at once.
    plt.figure()
    scatter = plt.scatter(x, y, c=color_values, s=100, cmap="viridis")
    plt.colorbar(scatter, label=color_label)
    plt.xlabel("Area (sq ft)")
    plt.ylabel("Price (Lakhs)")
    plt.title("House Price Analysis")
    plt.savefig(filename)
    plt.close()


def plot_scatter_with_size(x: np.ndarray, y: np.ndarray, size_values: np.ndarray, filename: str) -> None:
    # I encode a fourth variable as point size.
    plt.figure()
    # I scale up the raw values so they're visible as point sizes.
    sizes = size_values * 20
    plt.scatter(x, y, s=sizes, alpha=0.6, color="orangered")
    plt.xlabel("Experience (years)")
    plt.ylabel("Salary (thousands)")
    plt.title("Salary vs Experience (size = team size)")
    plt.savefig(filename)
    plt.close()


# --- TESTING ---

hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks = np.array([35, 42, 50, 55, 60, 68, 75, 80, 88, 95])
plot_basic_scatter(hours_studied, marks, "Hours Studied", "Marks", "day43_scatter.png")

area = np.array([800, 1200, 1500, 2000, 2500, 1800, 2200])
price = np.array([40, 60, 75, 95, 120, 85, 105])
bedrooms = np.array([1, 2, 2, 3, 4, 3, 3])
plot_scatter_with_color(area, price, bedrooms, "Bedrooms", "day43_scatter_color.png")

experience = np.array([1, 3, 5, 7, 10, 12])
salary = np.array([30, 45, 60, 75, 95, 110])
team_size = np.array([2, 4, 6, 8, 10, 12])
plot_scatter_with_size(experience, salary, team_size, "day43_scatter_size.png")

print("All 3 scatter plots saved successfully.")

