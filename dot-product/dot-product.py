import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    assert len(x) == len(y)

    n = len(x)
    result = 0.0

    for i in range(n):
        result = result + x[i] * y[i]

    return result