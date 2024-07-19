import math


def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    sum_exp_scores = sum(exp_scores)
    probabilities = [round(exp / sum_exp_scores, 4) for exp in exp_scores]
    return probabilities
