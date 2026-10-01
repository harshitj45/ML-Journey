# ============================================
# Day 43 - Program 127
# Topic: plt.subplots() — Multiple Charts Together
# Concepts: creating a grid of plots, customizing
#           each axis individually, tight_layout
# ============================================

import matplotlib.pyplot as plt
import numpy as np


def build_sample_data() -> dict:
    # I build a small set of related data to visualize together,
    # like a simple analytics dashboard would.
    return {
        "months": ["Jan", "Feb", "Mar", "Apr", "May"],
        "sales": [100, 120, 90, 150, 200],
        "cities": ["Delhi", "Mumbai", "Chennai"],
        "revenue": [500, 700, 300],
        "marks": np.random.normal(70, 10, 300),
        "hours": np.array([1, 2, 3, 4, 5, 6, 7, 8]),
        "scores": np.array([35, 42, 50, 55, 60, 68, 75, 80]),
    }


def build_two_chart_dashboard(data: dict, filename: str) -> None:
    # I place a line chart and a bar chart side by side.
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(data["months"], data["sales"], marker="o")
    axes[0].set_title("Sales Trend")
    axes[0].set_xlabel("Month")

    axes[1].bar(data["cities"], data["revenue"], color="green")
    axes[1].set_title("Revenue by City")

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def build_four_chart_dashboard(data: dict, filename: str) -> None:
    # I place four different chart types in a 2x2 grid,
    # each customized on its own axis.
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    axes[0, 0].plot(data["months"], data["sales"], marker="o", color="steelblue")
    axes[0, 0].set_title("Sales Trend")

    axes[0, 1].bar(data["cities"], data["revenue"], color="coral")
    axes[0, 1].set_title("Revenue by City")

    axes[1, 0].hist(data["marks"], bins=20, color="mediumseagreen")
    axes[1, 0].set_title("Marks Distribution")

    axes[1, 1].scatter(data["hours"], data["scores"], color="darkorange")
    axes[1, 1].set_title("Hours vs Scores")

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


# --- TESTING ---

np.random.seed(1)
data = build_sample_data()

build_two_chart_dashboard(data, "day43_dashboard_2.png")
build_four_chart_dashboard(data, "day43_dashboard_4.png")

print("Dashboards saved: day43_dashboard_2.png, day43_dashboard_4.png")

