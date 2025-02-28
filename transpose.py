def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    #    if not a or not a[0]:
    #        return []
    #
    #    rows, cols = len(a), len(a[0])
    #    b = [[0 for _ in range(rows)] for _ in range(cols)]
    #
    #    for i in range(rows):
    #        for j in range(cols):
    #            b[j][i] = a[i][j]
    #
    #    return b

    # Instead of making another list b, transpose could be done
    # like this-

    return [list(i) for i in zip(*a)]


# zip(*a) does the transpose but it returns
# a tuple.
