import pandas as pd

# 1. Data load aur merge karna
orders = pd.read_csv("data/olist_orders_dataset.csv")
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
merged = pd.merge(orders, reviews, on="order_id", how="inner")

# 2. Step 1: Missing Text Flag banana
merged["has_review_text"] = merged["review_comment_message"].notna()

print("=== REVIEW TEXT COUNT ===")
print(merged["has_review_text"].value_counts())

# 3. Step 2: Kis rating par log zyada text likhte hain?
print("\n=== PERCENTAGE WHO WROTE TEXT BY RATING ===")
text_pct_by_score = (
    merged.groupby("review_score")["has_review_text"].mean() * 100
).round(1)
print(text_pct_by_score)

# 4. Step 3: NLP (Project 3) ke liye usable text subset
text_reviews = merged[merged["has_review_text"]].copy()

print("\n=== TEXT SUBSET STATS ===")
print(f"Total merged rows: {len(merged)}")
print(f"Usable text reviews: {len(text_reviews)}")
print(f"Percentage usable: {len(text_reviews)/len(merged)*100:.1f}%")

print("\n=== SAMPLE TEXT REVIEWS ===")
print(text_reviews[["review_score", "review_comment_message"]].sample(3))

