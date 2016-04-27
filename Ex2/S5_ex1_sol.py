import numpy as np
from backend import show_tensor
import scipy

"""
Read numpy matrix S5A and S5B as A and B,
obtain their matrix product as C,
transpose C,
obtain its matrix inverse,
visualize the result with show_tensor
"""

A = np.load('S5A.npy')
B = np.load('S5B.npy')

C = np.dot(A,B)
C = C.T

C = np.linalg.inv(C)

show_tensor({'C':C})