# ============================================
# Day 43 - Program 125
# Topic: Line, Bar, Histogram Plots
# Concepts: plt.plot with labels/legend, plt.bar,
#           plt.hist with bins, saving figures
# ============================================

import matplotlib.pyplot as plt
import numpy as np


def plot_sales_trend(months: list, sales: list, filename: str) -> None:
    # I plot a simple line chart showing sales over time.
    plt.figure()
    plt.plot(months, sales, marker="o", color="steelblue")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales Trend")
    plt.savefig(filename)
    plt.close()


def plot_product_comparison(months: list, product_a: list, product_b: list, filename: str) -> None:
    # I plot two lines on the same chart to compare two products.
    plt.figure()
    plt.plot(months, product_a, label="Product A", marker="o")
    plt.plot(months, product_b, label="Product B", marker="s")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Product Comparison")
    plt.legend()
    plt.savefig(filename)
    plt.close()


def plot_city_revenue(cities: list, revenue: list, filename: str) -> None:
    # I plot a bar chart comparing revenue across categories.
    plt.figure()
    plt.bar(cities, revenue, color="coral")
    plt.xlabel("City")
    plt.ylabel("Revenue")
    plt.title("Revenue by City")
    plt.savefig(filename)
    plt.close()


def plot_marks_distribution(marks: np.ndarray, filename: str) -> None:
    # I plot a histogram to see the shape of a distribution.
    plt.figure()
    plt.hist(marks, bins=20, color="mediumseagreen", edgecolor="black")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title("Marks Distribution")
    plt.savefig(filename)
    plt.close()


# --- TESTING ---

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 90, 150, 200]
plot_sales_trend(months, sales, "day43_line.png")

product_a = [100, 120, 90, 150, 200]
product_b = [80, 100, 110, 130, 170]
plot_product_comparison(months, product_a, product_b, "day43_multiline.png")

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore"]
revenue = [50000, 70000, 30000, 60000]
plot_city_revenue(cities, revenue, "day43_bar.png")

np.random.seed(1)
marks = np.random.normal(loc=70, scale=10, size=500)
plot_marks_distribution(marks, "day43_hist.png")

print("All 4 plots saved successfully.")

