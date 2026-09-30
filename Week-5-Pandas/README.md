# Week 5 — Pandas

## Topics Covered

| Day | Topic |
|-----|-------|
| Day 33 | Series + DataFrame Basics |
| Day 34 | loc vs iloc Deep Dive + Multi-Condition Filtering |
| Day 35 | Add/Rename/Drop Columns + apply() |
| Day 36 | Missing Values Detection + Handling |
| Day 37 | Outlier Detection (IQR) + Duplicates + Data Type Fixing |
| Day 38 | Sorting, Ranking, value_counts, unique Analysis |
| Day 39 | GroupBy + Aggregation + pivot_table |
| Day 40 | Merge (All Join Types) + Concat |
| Day 41 | Time Series (resample/rolling/shift) + String Operations |
| Day 42 | Week 5 Mini Project |

**31 programs (94-124) across 10 days.**

## Concepts Used

- Series/DataFrame creation (3 ways), exploration (head/info/describe)
- loc vs iloc, multi-condition filtering, safe editing with .loc
- Column operations, apply() (Series + row-wise), apply vs vectorized
- isna/notna, sentinel values, dropna/fillna strategies
- IQR outlier detection, clip(), duplicated/drop_duplicates
- astype, to_numeric/to_datetime with errors="coerce"
- sort_values, rank, value_counts, unique/nunique
- groupby, .agg() (list + dict + custom function), pivot_table, reset_index
- merge (inner/left/right/outer), left_on/right_on, indicator=True
- concat (axis=0/1), ignore_index
- resample, rolling, shift, .str accessor (strip/lower/contains/split/extract)

## Mini Project — E-Commerce Sales Pipeline

### Description
A realistic messy-data pipeline: two raw tables (customers, orders)
with duplicates, missing values, bad dtypes, and outliers — cleaned,
merged, and analyzed into business insights (revenue by city, top
customers, weekly revenue trend).

### Files
- `data_sources.py` — intentionally messy raw data
- `data_cleaner.py` — string cleaning, dedup, type fixing, IQR capping
- `analysis.py` — merge with indicator, groupby, resample, rolling
- `day42_p124_main_pipeline.py` — runs the full pipeline + report

### How to Run
```bash
cd day42_project
python day42_p124_main_pipeline.py
```

### Author
Harshit | BTech CSE Final Year | ML Journey Week 5

