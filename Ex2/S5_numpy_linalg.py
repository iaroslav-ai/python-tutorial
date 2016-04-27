import numpy as np
from backend import show_tensor


# 2d array: matrix
M = np.random.rand(*(10,5))

# 1d array: vector
V = np.random.rand(5)

# transpose
show_tensor({'M':M, 'M.T':M.T})

# inner product
print np.dot(M,V)

#show_tensor({'M':M, 'V':V, 'dot':np.dot(M,V)})

M = np.random.rand(*(5,5))
V = np.random.rand(5)

print np.linalg.solve(M,V)