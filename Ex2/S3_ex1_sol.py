import numpy as np
from backend import show_tensor

"""
Load array S3.npy.
Add to every element of every column of S3 value such that
all elements of resulting array are positive and
minimum of every column is 0.
Show resulting array with show_tensor function
"""

A = np.load('S3.npy')
mn = np.min(A, axis=0)
R = A - mn

show_tensor({'R':R, 'A':A})