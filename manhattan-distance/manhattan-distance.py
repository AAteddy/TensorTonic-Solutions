import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """

    assert len(x) == len(y)

    n = len(x)
    result = 0.0

    for i in range(n):
        result = result + abs(x[i] - y[i])

    return result
    