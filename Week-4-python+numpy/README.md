# Week 4 — Maths for ML + NumPy Fundamentals

## Topics Covered

| Day | Topic |
|-----|-------|
| Day 22 | Vectors Deep Dive — L1/L2 Norms, Cosine Similarity, Broadcasting |
| Day 23 | Matrices Deep Dive — Determinant, Inverse, Eigenvalues, Covariance |
| Day 24 | Descriptive Statistics — Skewness, Distributions, Z-Score |
| Day 25 | Probability + Bayes Theorem — Naive Bayes Classifier |
| Day 26 | Correlation Deep Dive — Spearman, Hypothesis Testing, t-tests |
| Day 27 | Calculus — Derivatives, Chain Rule, Gradient Descent |
| Day 28 | Mini Project — Linear Regression from Scratch |
| Day 29 | Full Self-Assessment + Synthesis Challenges |
| Day 30 | NumPy — Array Creation, Reshaping, Stacking & Splitting |
| Day 31 | NumPy — Views vs Copies, Fancy & Boolean Indexing |
| Day 32 | Week 4 Capstone — Data Preparation Pipeline |

**33 programs written across 11 days**, closing out the full Maths + NumPy foundation for ML.

---

## Concepts Used

### Linear Algebra
- L1 (Manhattan) and L2 (Euclidean) norms, unit vectors
- Cosine similarity, vectorized distance calculations via broadcasting
- Determinant, matrix inverse, solving linear systems (`np.linalg.solve`)
- Eigenvalues and eigenvectors, covariance matrices

### Statistics
- Population vs sample variance (`ddof`), skewness
- Normal, Bernoulli, and Binomial distributions, the 68-95-99.7 rule
- Z-score standardization and outlier detection
- Spearman rank correlation, correlation vs causation
- Hypothesis testing, p-values, independent-samples t-tests

### Probability
- Conditional probability, independence
- Bayes' Theorem (prior, likelihood, posterior)
- Naive Bayes text classifier built from scratch

### Calculus
- Derivatives (power rule), numerical (finite-difference) derivatives
- Partial derivatives, the gradient vector
- Chain rule — the basis of backpropagation
- Gradient descent, learning rate effects, batch/SGD/mini-batch

### NumPy — Array Mechanics
- Array creation: `zeros`, `ones`, `full`, `eye`, `arange`, `linspace`
- Reshaping: `reshape`, `-1` auto-dimension, `flatten` vs `ravel`
- Combining and splitting: `vstack`, `hstack`, `concatenate`, `hsplit`, `vsplit`
- Views vs copies: `np.shares_memory`, `.base`, explicit `.copy()`
- Fancy indexing, boolean indexing (`&` `|` `~`), `np.where`, `np.unique`

---

## Milestone Projects

### 1. Linear Regression from Scratch (Day 28)
A multi-feature linear regression model trained with gradient descent, following the same `fit()` / `predict()` / `score()` interface as Scikit-learn — standardization, vectorized gradients, and R² evaluation, all implemented from first principles.

**Files:** `ml_math_utils.py`, `linear_regression_scratch.py`, `day28_p81_main_demo.py`

### 2. Full Self-Assessment + Synthesis Challenges (Day 29)
Active-recall test across all of Python (Day 1-18) and Maths (Day 19-28), followed by three synthesis challenges combining concepts across multiple weeks: a dataset quality checker, a similarity-based student finder, and a config-driven gradient descent trainer.

### 3. Data Preparation Pipeline (Day 32)
A realistic data-cleaning pipeline: combining multiple raw sources, removing invalid and outlier entries with boolean indexing, reordering with fancy indexing, labeling with `np.where`, and a manual train/test split — closing out the array-mechanics side of Week 4.

**Files:** `data_sources.py`, `data_cleaner.py`, `day32_p93_main_pipeline.py`

---

## How to Run

Each mini-project's files must be in the same folder before running:

```bash
cd day28_project
python day28_p81_main_demo.py

cd day32_project
python day32_p93_main_pipeline.py
```

---

## Key Takeaway

Every algorithm used later via libraries — `MinMaxScaler`, `MultinomialNB`, gradient-based optimizers, `train_test_split` — was implemented here first from raw NumPy and Python, so the underlying math is never a black box going forward.

---

## Author
Harshit Jain | BTech CSE Final Year | ML Journey Week 4