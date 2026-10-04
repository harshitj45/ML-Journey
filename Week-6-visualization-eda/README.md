# Week 6 — Data Visualization (Matplotlib/Seaborn) + EDA Framework

## Topics Covered

| Day | Topic |
|-----|-------|
| Day 43 | Matplotlib Basics — Line, Bar, Histogram, Scatter, Subplots |
| Day 44 | Seaborn — Boxplot, Heatmap, Pairplot, Countplot |
| Day 45 | Full 8-Step EDA Framework |

**9 programs (125–133) across 3 days**, closing out the visualization and EDA foundation used directly in Project 1.

---

## Concepts Used

### Matplotlib
- Line charts (`plt.plot`) with markers, labels, and `legend()`
- Bar charts (`plt.bar` / `plt.barh`) for category comparison
- Histograms (`plt.hist`, `bins=`) for distribution shape
- Scatter plots (`plt.scatter`), encoding extra dimensions with `c=` (color) and `s=` (size)
- Multi-chart dashboards with `plt.subplots()` and `tight_layout()`
- Saving figures correctly (`savefig()` before `show()`/`close()`)

### Seaborn
- `sns.boxplot()` — visualizing IQR and outliers directly (ties to Day 37's IQR method)
- `sns.heatmap()` on `df.corr()` — visualizing correlation (ties to Day 23's `np.corrcoef()`)
- `sns.pairplot()` — every numeric feature pair in one grid, with `hue=` for category coloring
- `sns.countplot()` — visual version of Day 38's `value_counts()`
- `sns.histplot(kde=True)` — histogram with a smooth density curve overlay

### 8-Step EDA Framework
1. **Overview** — shape, dtypes, nulls, duplicates
2. **Univariate Analysis** — each feature's own distribution/frequency
3. **Bivariate Analysis** — feature pairs (scatter, boxplot, groupby)
4. **Multivariate Analysis** — correlation heatmap, pairplot across all features
5. **Outlier Analysis** — confirming outliers with the IQR method
6. **Missing Value Patterns** — checking *why* values are missing, not just counting them
7. **Feature Hypothesis** — guessing which features matter, before any model
8. **Written Conclusions** — turning charts into plain-English findings (the most-skipped, most-valuable step)

---

## Milestone

This week has no standalone mini-project — instead, the 8-step framework built on Day 45 was applied directly to **Project 1** (Olist E-Commerce EDA), which lives in its own folder with its own README and full findings.

📁 See [`day46_project1/`](../day46_project1) for the applied, real-dataset version of this framework.

---

## How to Run

```bash
cd Week-6-visualization-eda
python day43_p125_basic_plots.py
python day44_p128_boxplot_heatmap.py
python day45_p131_eda_overview_univariate.py
# (and so on for each day's programs)
```

Program 132 and 133 (Day 45) import from `day45_p131_eda_overview_univariate.py`, so all three Day 45 files must stay in the same folder.

---

## Key Takeaway

Every chart type learned this week maps to a specific step in the EDA framework — boxplots confirm outliers, heatmaps confirm correlation, countplots confirm frequency. Nothing here is decorative; each visualization answers a specific question the framework asks.

---

## Author
Harshit | BTech CSE Final Year | ML Journey Week 6
