import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    X = np.column_stack((np.ones(X.shape[0]), X))

    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    # Round off to 4 decimal places
    theta = np.round(theta, 4)

    return theta.tolist()
