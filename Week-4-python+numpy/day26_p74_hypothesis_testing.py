# ============================================
# Day 26 - Program 74
# Topic: Hypothesis Testing and t-tests
# Concepts: t-statistic formula, scipy p-value,
#           significance level decision
# ============================================

import numpy as np
from scipy import stats


def calculate_t_statistic(group1: np.ndarray, group2: np.ndarray) -> float:
    # I calculate the t-statistic manually using the
    # difference in means, scaled by the combined
    # standard error of both groups.
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    n1, n2 = len(group1), len(group2)

    return (mean1 - mean2) / np.sqrt(var1 / n1 + var2 / n2)


def run_t_test(group1: np.ndarray, group2: np.ndarray) -> dict:
    # I use scipy to get the t-statistic and p-value
    # together, since computing the p-value by hand
    # requires the t-distribution's CDF.
    t_stat, p_value = stats.ttest_ind(group1, group2)
    return {"t_statistic": t_stat, "p_value": p_value}


def is_significant(p_value: float, alpha: float = 0.05) -> bool:
    # I decide whether to reject the null hypothesis
    # based on the chosen significance level.
    return p_value < alpha


def compare_groups(group1: np.ndarray, group2: np.ndarray,
                    label1: str, label2: str, alpha: float = 0.05) -> None:
    # I run a full comparison and print a readable conclusion.
    manual_t = calculate_t_statistic(group1, group2)
    result = run_t_test(group1, group2)
    significant = is_significant(result["p_value"], alpha)

    print(f"Comparing {label1} vs {label2}")
    print(f"  Manual t-statistic: {manual_t:.4f}")
    print(f"  Scipy t-statistic: {result['t_statistic']:.4f}")
    print(f"  P-value: {result['p_value']:.4f}")

    if significant:
        print(f"  I reject H0 — there IS a significant difference")
    else:
        print(f"  I fail to reject H0 — no significant difference found")


# --- TESTING ---

model_a_scores = np.array([0.85, 0.87, 0.86, 0.84, 0.88, 0.85, 0.86])
model_b_scores = np.array([0.82, 0.83, 0.81, 0.84, 0.80, 0.82, 0.83])

compare_groups(model_a_scores, model_b_scores, "Model A", "Model B")

# I test with two groups that are actually very similar.
group_x = np.array([0.85, 0.86, 0.84, 0.87, 0.85])
group_y = np.array([0.86, 0.84, 0.85, 0.86, 0.85])

compare_groups(group_x, group_y, "Group X", "Group Y")

