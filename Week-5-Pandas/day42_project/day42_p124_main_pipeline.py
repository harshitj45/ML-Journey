# ============================================
# Day 42 - Program 124 (Main)
# Topic: Week 5 Capstone — Full E-Commerce Pipeline
# Concepts: combining every Pandas skill from
#           Days 33-41 into one realistic workflow
# ============================================

from data_sources import build_raw_customers, build_raw_orders
from data_cleaner import clean_customers, full_clean_orders
from analysis import (
    merge_customers_orders, find_unmatched, revenue_by_city,
    top_customers, weekly_revenue_trend, rolling_revenue,
    week_over_week_change
)


def print_section(title: str) -> None:
    print(f"\n{'=' * 45}\n{title}\n{'=' * 45}")


# --- STEP 1: LOAD RAW DATA ---
print_section("Raw Data")
raw_customers = build_raw_customers()
raw_orders = build_raw_orders()
print(f"Raw customers:\n{raw_customers}")
print(f"\nRaw orders:\n{raw_orders}")

# --- STEP 2: CLEAN ---
print_section("Cleaned Data")
customers = clean_customers(raw_customers)
orders = full_clean_orders(raw_orders)
print(f"Cleaned customers:\n{customers}")
print(f"\nCleaned orders:\n{orders}")

# --- STEP 3: MERGE ---
print_section("Merged Data")
merged = merge_customers_orders(customers, orders)
print(merged)

unmatched = find_unmatched(merged)
print(f"\nUnmatched rows (missing on one side):\n{unmatched[['customer_id', 'name', 'order_id', '_merge']]}")

# --- STEP 4: BUSINESS ANALYSIS ---
print_section("Revenue by City")
print(revenue_by_city(merged))

print_section("Top Customers")
print(top_customers(merged, n=3))

print_section("Weekly Revenue Trend")
weekly = weekly_revenue_trend(merged)
print(weekly)

print_section("Rolling Average Revenue")
print(rolling_revenue(weekly))

print_section("Week-over-Week Change")
print(week_over_week_change(weekly))

