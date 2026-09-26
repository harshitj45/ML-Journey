# ============================================
# Day 40 - Program 115
# Topic: All Four Merge Join Types
# Concepts: inner, left, right, outer joins,
#           predicting row counts before merging
# ============================================

import pandas as pd


def build_customers() -> pd.DataFrame:
    # I build a customers table with one customer who has no orders.
    return pd.DataFrame({
        "customer_id": [1, 2, 3],
        "name": ["Harshit", "Priya", "Rahul"],
    })


def build_orders() -> pd.DataFrame:
    # I build an orders table with one order for a customer
    # that doesn't exist in the customers table.
    return pd.DataFrame({
        "order_id": [101, 102, 103, 104],
        "customer_id": [1, 2, 1, 4],
        "amount": [500, 300, 700, 200],
    })


def inner_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I keep only rows where the customer_id exists in both tables.
    return pd.merge(customers, orders, on="customer_id", how="inner")


def left_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I keep every customer, even those with no matching orders.
    return pd.merge(customers, orders, on="customer_id", how="left")


def right_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I keep every order, even those with no matching customer.
    return pd.merge(customers, orders, on="customer_id", how="right")


def outer_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # I keep everything from both tables.
    return pd.merge(customers, orders, on="customer_id", how="outer")


def compare_row_counts(customers: pd.DataFrame, orders: pd.DataFrame) -> dict:
    # I predict-and-verify the row count for every join type at once.
    counts = {}
    for how in ["inner", "left", "right", "outer"]:
        result = pd.merge(customers, orders, on="customer_id", how=how)
        counts[how] = result.shape[0]
    return counts


# --- TESTING ---

customers = build_customers()
orders = build_orders()

print(f"Inner join:\n{inner_join(customers, orders)}")
print(f"\nLeft join:\n{left_join(customers, orders)}")
print(f"\nRight join:\n{right_join(customers, orders)}")
print(f"\nOuter join:\n{outer_join(customers, orders)}")

counts = compare_row_counts(customers, orders)
print(f"\nRow counts by join type: {counts}")

