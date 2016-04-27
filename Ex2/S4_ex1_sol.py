import numpy as np
from backend import show_tensor

A = np.zeros((10,10))

"""
Modify matrix A such that you get the same output as in S4.png
Do NOT use for loops
Smaller number of lines is better
"""

A[1:9,1:9]=0.5
A[2:8,2:8]=1.0
A[3:7,3:7]=1.5

A[range(10), range(10)] = -2.0
A[9 - np.array(range(10)), range(10)] = -2.0

A[4:6,4:6]=1.5

A[:5,:5] = - A[:5,:5]
A[5:,5:] = - A[5:,5:]

show_tensor({'A':A})