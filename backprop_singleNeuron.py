import numpy as np


def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int,
) -> (np.ndarray, float, list[float]):
    weights = np.array(initial_weights)
    bias = initial_bias
    mse_values = []

    for _ in range(epochs):
        predictions = 1 / (1 + np.exp(-np.dot(features, weights) - bias))
        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(round(mse, 4))

        dw = np.mean(
            (predictions - labels) * predictions * (1 - predictions) * features.T,
            axis=1,
        )
        db = np.mean((predictions - labels) * predictions * (1 - predictions))

        weights -= learning_rate * dw
        bias -= learning_rate * db

    return np.round(weights, 4), round(bias, 4), mse_values
