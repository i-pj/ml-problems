def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = [sum(row) / len(row) for row in matrix]
    elif mode == "column":
        transposed_matrix = list(map(list, zip(*matrix)))
        means = [sum(col) / len(col) for col in transposed_matrix]
    return means
