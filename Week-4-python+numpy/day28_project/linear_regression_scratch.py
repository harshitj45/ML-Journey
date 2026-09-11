# ============================================
# Day 28 - Program 80
# Topic: Multi-Feature Linear Regression from Scratch
# Concepts: OOP fit/predict pattern, gradient descent
#           with matrix operations, standardization
# ============================================

import numpy as np
from ml_math_utils import standardize, apply_standardization, r_squared


class LinearRegressionScratch:
    # I build this class the same way sklearn structures
    # its models — with fit(), predict(), and score().

    def __init__(self, learning_rate: float = 0.01, epochs: int = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.train_mean = None
        self.train_std = None
        self.loss_history = []
        self.is_fitted = False

    def _predict_standardized(self, X: np.ndarray) -> np.ndarray:
        # I calculate predictions using matrix multiplication
        # instead of looping over each feature.
        return X @ self.weights + self.bias

    def fit(self, X: np.ndarray, y: np.ndarray):
        # I standardize the features first, using only
        # training data statistics, then train with
        # gradient descent.
        result = standardize(X)
        X_scaled = result["data"]
        self.train_mean = result["mean"]
        self.train_std = result["std"]

        n_samples, n_features = X_scaled.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for epoch in range(self.epochs):
            y_pred = self._predict_standardized(X_scaled)
            error = y_pred - y

            # I compute the gradients using the vectorized
            # form of the MSE partial derivatives.
            dw = (2 / n_samples) * (X_scaled.T @ error)
            db = (2 / n_samples) * np.sum(error)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            loss = np.mean(error ** 2)
            self.loss_history.append(loss)

        self.is_fitted = True
        return self   # I return self so fit() can be chained.

    def predict(self, X: np.ndarray) -> np.ndarray:
        # I standardize new data using the TRAINING mean and
        # std, never recalculating from the new data itself.
        if not self.is_fitted:
            raise Exception("I need to call fit() before predict().")
        X_scaled = apply_standardization(X, self.train_mean, self.train_std)
        return self._predict_standardized(X_scaled)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        # I evaluate the model using R-squared.
        y_pred = self.predict(X)
        return r_squared(y, y_pred)

    def __str__(self):
        if not self.is_fitted:
            return "LinearRegressionScratch (not trained yet)"
        return (f"LinearRegressionScratch(weights={self.weights.round(3)}, "
                f"bias={self.bias:.3f}, final_loss={self.loss_history[-1]:.4f})")

    