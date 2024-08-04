import numpy as np


def accuracy_score(y_true, y_pred):
    correct_predictions = np.sum(y_true == y_pred)

    total_predictions = len(y_true)

    accuracy = correct_predictions / total_predictions

    return accuracy
