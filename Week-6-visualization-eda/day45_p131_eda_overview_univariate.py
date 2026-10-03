# ============================================
# Day 45 - Program 131
# Topic: EDA Framework Steps 1-3
# Concepts: dataset overview, univariate analysis,
#           bivariate analysis — combining Days
#           33-44 into a systematic process
# ============================================

import pandas as pd
import numpy as np


def build_cafe_dataset() -> pd.DataFrame:
    # I build a synthetic cafe orders dataset with realistic
    # messiness — an outlier price, some missing ratings.
    np.random.seed(1)
    n = 100
    items = np.random.choice(["Coffee", "Tea", "Sandwich", "Pastry"], n)
    customer_type = np.random.choice(["Regular", "New"], n, p=[0.7, 0.3])
    price = np.where(items == "Sandwich", np.random.uniform(80, 120, n),
                     np.random.uniform(30, 70, n))
    price[5] = 500  # I plant one obvious outlier
    quantity = np.random.randint(1, 5, n)
    rating = np.random.randint(1, 6, n).astype(float)
    rating[np.random.choice(n, 10, replace=False)] = np.nan  # missing ratings

    return pd.DataFrame({
        "item": items, "customer_type": customer_type,
        "price": price, "quantity": quantity, "rating": rating,
    })


def step1_overview(df: pd.DataFrame) -> None:
    # STEP 1: I check the overall structure before anything else.
    print("--- STEP 1: Dataset Overview ---")
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\n{df.dtypes}")
    print(f"Missing values:\n{df.isna().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print(f"Numeric summary:\n{df.describe()}")


def step2_univariate(df: pd.DataFrame) -> None:
    # STEP 2: I look at each feature on its own.
    print("\n--- STEP 2: Univariate Analysis ---")
    print(f"Item frequency:\n{df['item'].value_counts()}")
    print(f"\nPrice stats: mean={df['price'].mean():.1f}, "
          f"median={df['price'].median():.1f}")
    skew_signal = "right-skewed" if df['price'].mean() > df['price'].median() else "left-skewed"
    print(f"Price appears {skew_signal} (mean vs median)")


def step3_bivariate(df: pd.DataFrame) -> None:
    # STEP 3: I check how pairs of features relate to each other.
    print("\n--- STEP 3: Bivariate Analysis ---")
    by_customer = df.groupby("customer_type")["rating"].mean()
    print(f"Average rating by customer type:\n{by_customer}")
    by_item_price = df.groupby("item")["price"].mean()
    print(f"\nAverage price by item:\n{by_item_price}")


# --- RUN ---

data = build_cafe_dataset()
step1_overview(data)
step2_univariate(data)
step3_bivariate(data)