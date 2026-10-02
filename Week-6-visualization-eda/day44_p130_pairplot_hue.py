# ============================================
# Day 44 - Program 130
# Topic: pairplot and the hue Parameter
# Concepts: sns.pairplot basic, sns.pairplot with
#           hue, hue reused across boxplot/scatterplot
# ============================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def build_student_dataset() -> pd.DataFrame:
    # I build a dataset with a category column (result) that
    # I can use to color every plot with hue=.
    np.random.seed(1)
    hours = np.concatenate([np.random.uniform(1, 4, 10), np.random.uniform(5, 9, 10)])
    attendance = hours * 8 + np.random.normal(0, 5, 20)
    marks = hours * 9 + np.random.normal(0, 4, 20)
    result = np.where(marks >= 50, "Pass", "Fail")
    return pd.DataFrame({
        "hours_studied": hours.round(1),
        "attendance": attendance.round(1),
        "marks": marks.round(1),
        "result": result,
    })


def plot_basic_pairplot(df: pd.DataFrame, filename: str) -> None:
    # I plot every numeric column against every other one.
    grid = sns.pairplot(df)
    grid.savefig(filename)
    plt.close()


def plot_pairplot_with_hue(df: pd.DataFrame, hue_column: str, filename: str) -> None:
    # I color every point by a category, making patterns
    # between Pass/Fail visible across every feature pair.
    grid = sns.pairplot(df, hue=hue_column)
    grid.savefig(filename)
    plt.close()


def plot_boxplot_with_hue(df: pd.DataFrame, filename: str) -> None:
    # I reuse the same hue idea on a boxplot, confirming
    # hue= works consistently across Seaborn plot types.
    plt.figure()
    sns.boxplot(data=df, x="result", y="hours_studied")
    plt.title("Hours Studied by Result")
    plt.savefig(filename)
    plt.close()


# --- TESTING ---

data = build_student_dataset()
print(f"Dataset:\n{data}")

plot_basic_pairplot(data, "day44_pairplot_basic.png")
plot_pairplot_with_hue(data, "result", "day44_pairplot_hue.png")
plot_boxplot_with_hue(data, "day44_boxplot_hue.png")

print("All pairplot and boxplot visuals saved successfully.")

