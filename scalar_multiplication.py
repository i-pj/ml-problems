def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    result = []
    for row in matrix:
        new_row = [scalar * element for element in row]
        result.append(new_row)
    return result
