# ============================================
# Day 49 - Project 1: Verification Checks
# Topic: Olist EDA, final checks before conclusions
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders = pd.read_csv("data/olist_orders_dataset.csv")
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")

# I convert the timestamp columns so I can do date arithmetic.
date_cols = ["order_purchase_timestamp", "order_delivered_customer_date",
             "order_estimated_delivery_date"]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# I recreate the delivery features engineered on Day 47.
orders["delivery_days"] = (orders["order_delivered_customer_date"]
                           - orders["order_purchase_timestamp"]).dt.days
orders["delivery_delay"] = (orders["order_delivered_customer_date"]
                            - orders["order_estimated_delivery_date"]).dt.days

merged = pd.merge(orders, reviews, on="order_id", how="inner")

# CHECK 1: I test whether some orders have more than one review.
print("=== CHECK 1: Reviews per order ===")
print("Review rows:", len(reviews), "| Unique order_ids:", reviews["order_id"].nunique())

# CHECK 2: I test whether lateness behaves like a threshold effect.
# NaN > 0 evaluates to False, so I drop undelivered orders first.
delivered = merged.dropna(subset=["delivery_delay"]).copy()
delivered["is_late"] = delivered["delivery_delay"] > 0
print("\n=== CHECK 2: % late orders by review score ===")
print((delivered.groupby("review_score")["is_late"].mean() * 100).round(1))
print("\nMedian delay by review score:")
print(delivered.groupby("review_score")["delivery_delay"].median())

# CHECK 3: I compare the score mix of text reviews and their length.
merged["has_review_text"] = merged["review_comment_message"].notna()
text_reviews = merged[merged["has_review_text"]].copy()
print("\n=== CHECK 3: Score share (%) among text reviews ===")
print((text_reviews["review_score"].value_counts(normalize=True)
       .sort_index() * 100).round(1))
text_reviews["review_length"] = text_reviews["review_comment_message"].str.len()
print("\nMedian review length by score:")
print(text_reviews.groupby("review_score")["review_length"].median())

# CHECK 4: I complete framework steps 4 and 5 (multivariate + outliers).
print("\n=== CHECK 4: Correlation and outliers ===")
corr = delivered[["review_score", "delivery_days", "delivery_delay"]].corr()
print(corr.round(2))
plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation: Review Score vs Delivery Metrics")
plt.savefig("day49_correlation.png")
plt.close()

q1 = delivered["delivery_days"].quantile(0.25)
q3 = delivered["delivery_days"].quantile(0.75)
upper = q3 + 1.5 * (q3 - q1)
print("Upper outlier bound (delivery_days):", upper)
print("Outlier orders:", (delivered["delivery_days"] > upper).sum())