from . import gcd
from . import inv_number_modulo
from . import cofactors_matrix
import numpy as np


def inv_matrix_modulo(A, m):
    det_A = np.linalg.det(A)
    inv_A = np.zeros((A.shape))
    if A.shape[0] == A.shape[1]:
        if gcd.gcd(round(det_A), m) == 1:
            inv_det_A = inv_number_modulo.inv_number_modulo(round(det_A), m)
            cofactors_A = cofactors_matrix.cofactors_matrix(A)
            inv_A = inv_det_A * cofactors_A
        else:
            raise Exception(
                "The matrix A is not invertible mod m because A is not coprime to m")
    else:
        raise Exception("Matrix must be square")

    inv_A = inv_A % m
    return inv_A
