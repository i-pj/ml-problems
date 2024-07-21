import numpy as np


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    arr = np.array(a)
    reshaped_arr = arr.reshape(new_shape)
    reshaped_matrix = reshaped_arr.tolist()
    return reshaped_matrix
