import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    num_rows = len(A)
    num_col = len(A[0])

    transposed = []

    for i in range(num_col):
        new_row = []
        for j in range(num_rows):
            new_row.append(A[j][i])
        transposed.append(new_row)
    
    return np.array(transposed)
