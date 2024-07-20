import numpy as np


def transform_basis(B: list[list[float]], C: list[list[float]]) -> list[list[float]]:
    B_array = np.array(B)
    C_array = np.array(C)

    P = np.linalg.inv(C_array) @ B_array

    P_rounded = np.round(P, decimals=4).tolist()

    return P_rounded
