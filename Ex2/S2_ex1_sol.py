import numpy as np
from backend import show_tensor

"""
Load 2d array from file S2.npy as A.
Comupte minimum values for every row as B
Compute maximum values for every column as C
Sum them up elementwise, and add to every value of result
mean of A
show result with show_tensor
"""

A = np.load('S2.npy')

B = np.min(A, axis=1)
C = np.max(A, axis=0)

R = B + C + np.mean(A)

show_tensor({'Result':R})
