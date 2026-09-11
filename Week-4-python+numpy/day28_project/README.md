# Week 4 — Maths for ML (Linear Algebra + Statistics + Calculus)

## Topics Covered

| Day | Topic |
|-----|-------|
| Day 22 | Vectors Deep Dive — L1/L2 Norms, Cosine Similarity, Broadcasting |
| Day 23 | Matrices Deep Dive — Determinant, Inverse, Eigenvalues, Covariance |
| Day 24 | Descriptive Statistics — Skewness, Distributions, Z-Score |
| Day 25 | Probability + Bayes Theorem — Naive Bayes Classifier |
| Day 26 | Correlation Deep Dive — Spearman, Hypothesis Testing, t-tests |
| Day 27 | Calculus — Derivatives, Chain Rule, Gradient Descent |
| Day 28 | Week 4 Mini Project |

## Concepts Used

- L1/L2 norms, unit vectors, cosine similarity
- NumPy broadcasting for vectorized distance calculations
- Determinant, matrix inverse, solving linear systems
- Eigenvalues and eigenvectors
- Covariance and correlation matrices
- Population vs sample variance, skewness
- Normal, Bernoulli, and Binomial distributions
- Z-score standardization
- Conditional probability, independence, Bayes Theorem
- Naive Bayes classification from scratch
- Spearman correlation, correlation vs causation
- Hypothesis testing, p-values, t-tests
- Derivatives, partial derivatives, the gradient vector
- Chain rule and its connection to backpropagation
- Gradient descent and learning rate effects

## Mini Project — Linear Regression from Scratch

### Description
A multi-feature linear regression model built entirely from
scratch using gradient descent, following the same fit/predict/
score pattern used by scikit-learn. Combines standardization,
matrix operations, and a full evaluation report into one pipeline.

### Files
- `ml_math_utils.py` — reusable maths toolkit (norms, cosine
  similarity, standardization, correlation, R-squared)
- `linear_regression_scratch.py` — `LinearRegressionScratch` class
- `day28_p81_main_demo.py` — trains the model on a synthetic
  student dataset and prints a full evaluation report

### How to Run
```bash
cd day28_project
python day28_p81_main_demo.py
```

### Key Result
Implements `fit()`, `predict()`, and `score()` exactly like
scikit-learn's `LinearRegression`, but built from first
principles — standardization, matrix multiplication for
predictions, and gradient descent for training.

### Author
Harshit | BTech CSE 4rd Year | ML Journey Week 4

