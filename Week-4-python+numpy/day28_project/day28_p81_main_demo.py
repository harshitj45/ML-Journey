# ============================================
# Day 28 - Program 81
# Topic: Full Pipeline Demo and Evaluation Report
# Concepts: training, correlation-based evaluation,
#           residual statistics, full month capstone
# ============================================

import numpy as np
from linear_regression_scratch import LinearRegressionScratch
from ml_math_utils import correlation, l2_norm, cosine_similarity


def print_training_summary(model: LinearRegressionScratch) -> None:
    # I print how the loss changed from start to end of training.
    history = model.loss_history
    print("Training Summary")
    print(f"  Starting loss: {history[0]:.4f}")
    print(f"  Final loss:    {history[-1]:.4f}")
    print(f"  Loss reduced by: {(1 - history[-1]/history[0]) * 100:.1f}%")


def print_evaluation_report(model: LinearRegressionScratch,
                             X_test: np.ndarray, y_test: np.ndarray) -> None:
    # I build a full evaluation report combining several
    # concepts from across the month.
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred

    print("\nEvaluation Report")
    print(f"  R-squared score: {model.score(X_test, y_test):.4f}")
    print(f"  Correlation (actual vs predicted): {correlation(y_test, y_pred):.4f}")
    print(f"  Residual mean: {np.mean(residuals):.4f}")
    print(f"  Residual std: {np.std(residuals, ddof=1):.4f}")
    print(f"  Residual L2 norm: {l2_norm(residuals):.4f}")


# --- BUILD A SMALL STUDENT DATASET ---

np.random.seed(42)

n_students = 50
hours_studied = np.random.uniform(1, 10, n_students)
attendance_pct = np.random.uniform(50, 100, n_students)
prev_score = np.random.uniform(40, 95, n_students)

final_score = (
    5 * hours_studied +
    0.3 * attendance_pct +
    0.4 * prev_score +
    np.random.normal(0, 3, n_students)
)

X = np.column_stack([hours_studied, attendance_pct, prev_score])
y = final_score

# I split the data into training and test sets manually.
split = int(0.8 * n_students)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]


# --- TRAIN AND EVALUATE ---

model = LinearRegressionScratch(learning_rate=0.05, epochs=500)
model.fit(X_train, y_train)

print(model)
print_training_summary(model)
print_evaluation_report(model, X_test, y_test)

# I also demonstrate one of my utility functions directly,
# comparing two students' feature vectors for similarity.
student_a = X[0]
student_b = X[1]
print(f"\nSimilarity between student 0 and student 1: "
      f"{cosine_similarity(student_a, student_b):.4f}")