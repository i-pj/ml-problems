import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros(n)

    for _ in range(iterations):
        hypothesis = np.dot(X, theta)
        error = hypothesis - y
        gradient = (1 / m) * np.dot(X.T, error)
        theta = theta - alpha * gradient

    return np.round(theta, 4)
