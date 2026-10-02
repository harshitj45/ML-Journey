# ============================================
# Day 44 - Program 128
# Topic: Boxplot for Outliers, Heatmap for Correlation
# Concepts: sns.boxplot by category, df.corr(),
#           sns.heatmap with annot and cmap
# ============================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def build_salary_dataset() -> pd.DataFrame:
    # I build a dataset with an obvious outlier in one city.
    return pd.DataFrame({
        "city":   ["Delhi"] * 5 + ["Mumbai"] * 5,
        "salary": [30, 32, 31, 29, 90, 35, 33, 34, 36, 32],
    })


def build_correlation_dataset() -> pd.DataFrame:
    # I build a dataset where features are clearly related,
    # so the heatmap has something meaningful to show.
    np.random.seed(1)
    hours = np.arange(1, 21)
    attendance = hours * 5 + np.random.normal(0, 3, 20)
    marks = hours * 8 + np.random.normal(0, 5, 20)
    return pd.DataFrame({
        "hours_studied": hours,
        "attendance": attendance,
        "marks": marks,
    })


def plot_boxplot_by_category(df: pd.DataFrame, x: str, y: str, filename: str) -> None:
    # I plot a boxplot to visually spot outliers per category.
    plt.figure()
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"{y} Distribution by {x}")
    plt.savefig(filename)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, filename: str) -> pd.DataFrame:
    # I calculate the correlation matrix and visualize it as a heatmap.
    corr_matrix = df.corr()
    plt.figure()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.savefig(filename)
    plt.close()
    return corr_matrix


# --- TESTING ---

salary_data = build_salary_dataset()
plot_boxplot_by_category(salary_data, "city", "salary", "day44_boxplot.png")

corr_data = build_correlation_dataset()
corr_matrix = plot_correlation_heatmap(corr_data, "day44_heatmap.png")
print(f"Correlation matrix:\n{corr_matrix}")

print("Boxplot and heatmap saved successfully.")

