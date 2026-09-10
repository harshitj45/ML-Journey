# ============================================
# Day 27 - Program 77
# Topic: Multi-Parameter Gradient Descent
# Concepts: partial derivatives of MSE loss,
#           iterative weight and bias updates,
#           learning rate effects
# ============================================

import numpy as np


def predict(x: np.ndarray, w: float, b: float) -> np.ndarray:
    # I calculate predictions using a linear equation.
    return w * x + b


def compute_loss(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    # I calculate the mean squared error between
    # predictions and actual values.
    y_pred = predict(x, w, b)
    return np.mean((y_pred - y) ** 2)


def compute_gradients(x: np.ndarray, y: np.ndarray, w: float, b: float) -> tuple:
    # I calculate the partial derivatives of the loss
    # with respect to w and b, using the MSE gradient formulas.
    n = len(x)
    y_pred = predict(x, w, b)
    error = y_pred - y

    dw = (2 / n) * np.sum(error * x)
    db = (2 / n) * np.sum(error)
    return dw, db


def train_with_gradient_descent(x: np.ndarray, y: np.ndarray,
                                 lr: float = 0.01, epochs: int = 100) -> dict:
    # I train a linear model by repeatedly updating w and b
    # in the direction that reduces the loss.
    w, b = 0.0, 0.0
    loss_history = []

    for epoch in range(epochs):
        loss = compute_loss(x, y, w, b)
        loss_history.append(loss)

        dw, db = compute_gradients(x, y, w, b)
        w = w - lr * dw
        b = b - lr * db

    return {"w": w, "b": b, "loss_history": loss_history}


# --- TESTING ---

# I create data that follows y = 3x + 2 approximately.
np.random.seed(42)
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_data = 3 * x_data + 2 + np.random.normal(0, 0.5, size=8)

result = train_with_gradient_descent(x_data, y_data, lr=0.02, epochs=200)
print(f"Learned w: {result['w']:.4f} (true value: 3)")
print(f"Learned b: {result['b']:.4f} (true value: 2)")
print(f"Final loss: {result['loss_history'][-1]:.4f}")
print(f"Starting loss: {result['loss_history'][0]:.4f}")

# I compare different learning rates.
for lr in [0.001, 0.02, 0.5]:
    r = train_with_gradient_descent(x_data, y_data, lr=lr, epochs=200)
    print(f"lr={lr}: final w={r['w']:.4f}, final loss={r['loss_history'][-1]:.4f}")

