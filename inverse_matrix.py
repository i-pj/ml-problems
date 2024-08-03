def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a, b = matrix[0]
    c, d = matrix[1]

    det = a * d - b * c

    if det == 0:
        return None

    inv_det = 1 / det
    inverse = [[d * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]

    inverse = [[round(elem, 6) for elem in row] for row in inverse]

    return inverse
