# ============================================
# Day 26 - Program 75
# Topic: Applied Hypothesis Testing for Model Selection
# Concepts: combining correlation and hypothesis testing
#           into one decision-making report
# ============================================

import numpy as np
from scipy import stats


def calculate_t_statistic(group1: np.ndarray, group2: np.ndarray) -> float:
    # I calculate the t-statistic manually.
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    n1, n2 = len(group1), len(group2)
    return (mean1 - mean2) / np.sqrt(var1 / n1 + var2 / n2)


def build_comparison_report(model_a_scores: np.ndarray, model_b_scores: np.ndarray,
                             alpha: float = 0.05) -> dict:
    # I build a full report comparing two models,
    # combining descriptive stats with a hypothesis test.
    t_stat, p_value = stats.ttest_ind(model_a_scores, model_b_scores)

    report = {
        "model_a_mean": np.mean(model_a_scores),
        "model_b_mean": np.mean(model_b_scores),
        "model_a_std": np.std(model_a_scores, ddof=1),
        "model_b_std": np.std(model_b_scores, ddof=1),
        "t_statistic": t_stat,
        "p_value": p_value,
        "significant_difference": p_value < alpha,
    }
    return report


def recommend_model(report: dict) -> str:
    # I use the report to make a final recommendation.
    if not report["significant_difference"]:
        return "No significant difference — I would pick the simpler or cheaper model."

    if report["model_a_mean"] > report["model_b_mean"]:
        return "Model A is significantly better — I recommend Model A."
    else:
        return "Model B is significantly better — I recommend Model B."


def print_report(report: dict, recommendation: str) -> None:
    print("Model Comparison Report")
    print("-" * 30)
    print(f"Model A: mean={report['model_a_mean']:.4f}, std={report['model_a_std']:.4f}")
    print(f"Model B: mean={report['model_b_mean']:.4f}, std={report['model_b_std']:.4f}")
    print(f"t-statistic: {report['t_statistic']:.4f}")
    print(f"p-value: {report['p_value']:.4f}")
    print(f"Significant difference: {report['significant_difference']}")
    print(f"Recommendation: {recommendation}")


# --- TESTING ---

# I compare two clearly different models.
model_a = np.array([0.91, 0.92, 0.90, 0.93, 0.91, 0.92])
model_b = np.array([0.85, 0.84, 0.86, 0.83, 0.85, 0.84])

report1 = build_comparison_report(model_a, model_b)
recommendation1 = recommend_model(report1)
print_report(report1, recommendation1)

print()

# I compare two models that perform almost the same.
model_c = np.array([0.88, 0.87, 0.89, 0.88, 0.87])
model_d = np.array([0.87, 0.88, 0.86, 0.89, 0.88])

report2 = build_comparison_report(model_c, model_d)
recommendation2 = recommend_model(report2)
print_report(report2, recommendation2)

