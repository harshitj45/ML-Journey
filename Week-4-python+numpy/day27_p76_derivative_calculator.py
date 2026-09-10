# ============================================
# Day 27 - Program 76
# Topic: Analytical and Numerical Derivatives
# Concepts: power rule, numerical (finite difference)
#           derivative, partial derivatives, gradient vector
# ============================================

import numpy as np


def numerical_derivative(func, x: float, h: float = 1e-6) -> float:
    # I approximate the derivative using the finite
    # difference method, without needing symbolic calculus.
    return (func(x + h) - func(x - h)) / (2 * h)


def power_rule_derivative(coefficient: float, power: int) -> tuple:
    # I apply the power rule to a single term c*x^n.
    # I return the new coefficient and new power.
    new_coefficient = coefficient * power
    new_power = power - 1
    return new_coefficient, new_power


def partial_derivative(func, point: list, index: int, h: float = 1e-6) -> float:
    # I calculate the partial derivative with respect to
    # one variable, keeping all other variables fixed.
    point_plus = point.copy()
    point_minus = point.copy()
    point_plus[index] += h
    point_minus[index] -= h
    return (func(*point_plus) - func(*point_minus)) / (2 * h)


def compute_gradient(func, point: list) -> np.ndarray:
    # I build the full gradient vector by calculating
    # every partial derivative at a given point.
    gradient = []
    for i in range(len(point)):
        gradient.append(partial_derivative(func, point, i))
    return np.array(gradient)


# --- TESTING ---

def f_single(x):
    return x**2 - 4*x + 4

def f_analytical_derivative(x):
    return 2*x - 4

# I verify my manual derivative against the numerical one.
test_x = 5
print(f"Analytical: {f_analytical_derivative(test_x)}")
print(f"Numerical: {numerical_derivative(f_single, test_x):.4f}")

# I test the power rule on x^3.
coef, power = power_rule_derivative(1, 3)
print(f"Derivative of x^3 is {coef}x^{power}")

# I test partial derivatives on a two-variable function.
def f_multi(x, y):
    return x**2 + y**2

gradient_at_point = compute_gradient(f_multi, [3, 4])
print(f"Gradient at (3,4): {gradient_at_point}")

# I test with a function that has three variables.
def f_three(x, y, z):
    return x**2 + y**2 + z**2

gradient_3d = compute_gradient(f_three, [1, 2, 3])
print(f"Gradient at (1,2,3): {gradient_3d}")

