# ============================================
# Day 41 - Program 120
# Topic: String Operations with .str Accessor
# Concepts: strip/lower/title, contains, split
#           with expand=True, extract with regex
# ============================================

import pandas as pd


def build_messy_dataset() -> pd.DataFrame:
    # I build a dataset with messy, inconsistent text formatting.
    return pd.DataFrame({
        "name":      ["  Harshit  ", "PRIYA", " rahul", "Neha  "],
        "email":     ["harshit@gmail.com", "priya@yahoo.com",
                      "rahul@gmail.com", "neha@outlook.com"],
        "full_name": ["Harshit Sharma", "Priya Singh", "Rahul Kumar", "Neha Gupta"],
    })


def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    # I chain multiple string methods together to fully
    # clean the name column in one line.
    df = df.copy()
    df["name_clean"] = df["name"].str.strip().str.title()
    return df


def filter_by_email_provider(df: pd.DataFrame, provider: str) -> pd.DataFrame:
    # I filter rows where the email contains a specific provider name.
    return df[df["email"].str.contains(provider)]


def split_full_name(df: pd.DataFrame) -> pd.DataFrame:
    # I split a full name into separate first and last name columns.
    df = df.copy()
    parts = df["full_name"].str.split(" ", expand=True)
    df["first_name"] = parts[0]
    df["last_name"] = parts[1]
    return df


def extract_email_domain(df: pd.DataFrame) -> pd.DataFrame:
    # I extract just the domain name from each email address.
    df = df.copy()
    df["domain"] = df["email"].str.extract(r"@(\w+)")
    return df


def full_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    # I run every cleaning step together as one pipeline.
    df = clean_names(df)
    df = split_full_name(df)
    df = extract_email_domain(df)
    return df


# --- TESTING ---

data = build_messy_dataset()
print(f"Original:\n{data}")

cleaned = clean_names(data)
print(f"\nCleaned names:\n{cleaned[['name', 'name_clean']]}")

gmail_only = filter_by_email_provider(data, "gmail")
print(f"\nGmail users only:\n{gmail_only}")

with_split = split_full_name(data)
print(f"\nSplit names:\n{with_split[['full_name', 'first_name', 'last_name']]}")

full_result = full_cleaning_pipeline(data)
print(f"\nFull pipeline result:\n{full_result}")
