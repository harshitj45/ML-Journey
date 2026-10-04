import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------
# 1. DATA LOAD KARNA
# -------------------------------------------------------------
orders = pd.read_csv("data/olist_orders_dataset.csv")
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")

# -------------------------------------------------------------
# 2. STEP 1: OVERVIEW (Shape, Data Types, Missing Values)
# -------------------------------------------------------------
print("=== ORDERS OVERVIEW ===")
print("Shape (Rows, Columns):", orders.shape)
print("\nData Types:")
print(orders.dtypes)
print("\nMissing Values Count:")
print(orders.isna().sum())
print("\nFirst 5 Rows:")
print(orders.head())

print("\n" + "="*40 + "\n")

print("=== REVIEWS OVERVIEW ===")
print("Shape (Rows, Columns):", reviews.shape)
print("\nData Types:")
print(reviews.dtypes)
print("\nMissing Values Count:")
print(reviews.isna().sum())
print("\nFirst 5 Rows:")
print(reviews.head())

# -------------------------------------------------------------
# 3. STEP 2: DISTRIBUTIONS & PATTERNS
# -------------------------------------------------------------
print("\n=== ORDER STATUS DISTRIBUTION ===")
print(orders["order_status"].value_counts())

print("\n=== REVIEW SCORE DISTRIBUTION ===")
print(reviews["review_score"].value_counts().sort_index())

# -------------------------------------------------------------
# 4. STEP 3: VISUALIZATION (Chart Save)
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=reviews, x="review_score", hue="review_score", legend=False, palette="viridis")
plt.title("Review Score Distribution (Olist)")
plt.xlabel("Review Score (1 to 5)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("day46_review_scores.png")
print("\nChart saved as 'day46_review_scores.png' successfully!")

