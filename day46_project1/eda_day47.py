import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data load karna
orders = pd.read_csv("data/olist_orders_dataset.csv")
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")

# 2. Step 1: Date Columns Datetime mein convert karna
date_cols = [
    "order_purchase_timestamp", "order_approved_at",
    "order_delivered_carrier_date", "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

print("=== CONVERTED DATA TYPES ===")
print(orders[date_cols].dtypes)

# 3. Step 2: Feature Engineering (Delivery Metrics)
orders["delivery_days"] = (
    orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
).dt.days

orders["delivery_delay"] = (
    orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"]
).dt.days

print("\n=== DELIVERY METRICS SUMMARY ===")
print(orders[["delivery_days", "delivery_delay"]].describe())

# 4. Step 3: Orders aur Reviews ko Merge karna
merged = pd.merge(orders, reviews, on="order_id", how="inner")
print("\n=== MERGE STATS ===")
print(f"Merged shape: {merged.shape}")
print(f"Orders: {orders.shape[0]}, Reviews: {reviews.shape[0]}")

# 5. Step 4: Delay vs Review Score Analysis
print("\n=== AVERAGE DELAY BY REVIEW SCORE ===")
delay_by_score = merged.groupby("review_score")["delivery_delay"].mean()
print(delay_by_score)

# 6. Visualization Save Karna
plt.figure(figsize=(8, 5))
sns.boxplot(data=merged, x="review_score", y="delivery_delay", hue="review_score", palette="coolwarm", legend=False)
plt.axhline(y=0, color="red", linestyle="--", label="On-time delivery")
plt.title("Delivery Delay vs Review Score")
plt.xlabel("Review Score (1 to 5)")
plt.ylabel("Delivery Delay in Days (Negative = Early, Positive = Late)")
plt.ylim(-30, 30)  # Extreme outliers ko limit karke chart readable banane ke liye
plt.legend()
plt.tight_layout()
plt.savefig("day47_delay_vs_score.png")
print("\nChart saved as 'day47_delay_vs_score.png' successfully!")

