import sympy as sp
from sympy.physics.quantum import TensorProduct

def kron(*matrices):
    output = sp.eye(1)
    for i in range(len(matrices)):
        output = TensorProduct(output, matrices[i])
    return output

def identity(dim):
    if dim == 0:
        return sp.eye(1)
    else:
        return sp.eye(dim)