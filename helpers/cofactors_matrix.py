import numpy as np


def cofactors_matrix(A):
    rows, cols = A.shape
    C = np.zeros((rows, cols))
    if rows == cols:
        for i in range(rows):
            for j in range(cols):
                m1 = np.concatenate((A[:i, :j], A[:i, (j+1):cols]), axis=1)
                m2 = np.concatenate(
                    (A[(i+1):rows, :j], A[(i+1): rows, (j+1): cols]), axis=1)
                m = np.concatenate((m1, m2), axis=0)
                C[i][j] = round(np.linalg.det(m) * pow(-1, i+j))

    else:
        raise Exception("Matrix must be square")
    C = C.T
    return C
