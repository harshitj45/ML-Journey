# ============================================
# Day 42 - Program 121 (Module)
# Topic: Raw Messy Data Sources
# Concepts: intentionally messy data to clean —
#           duplicates, missing values, outliers,
#           bad dtypes, unclean strings
# ============================================

import pandas as pd


def build_raw_customers() -> pd.DataFrame:
    # I build a customers table with a duplicate row and
    # inconsistently formatted names and emails.
    return pd.DataFrame({
        "customer_id": [1, 2, 3, 3, 4],
        "name": ["  harshit sharma", "PRIYA SINGH", "Rahul Kumar", "Rahul Kumar", "neha  "],
        "email": ["Harshit@Gmail.com", "priya@YAHOO.com", "rahul@Gmail.com",
                  "rahul@Gmail.com", "neha@Outlook.com"],
        "city": ["Delhi", "Mumbai", "Delhi", "Delhi", "Chennai"],
    })


def build_raw_orders() -> pd.DataFrame:
    # I build an orders table with a missing amount, an
    # invalid date, an outlier amount, and an order for a
    # customer_id that doesn't exist in the customers table.
    return pd.DataFrame({
        "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "customer_id": [1, 2, 1, 3, 2, 4, 1, 5],
        "order_date": ["2026-01-05", "2026-01-08", "2026-01-15", "2026-01-20",
                       "2026-02-02", "2026-02-10", "2026-02-15", "invalid"],
        "amount": ["500", "300", "15000", "700", "abc", "450", "600", "200"],
    })
