import numpy as np
import matplotlib.pyplot as plt


X = np.random.randn(1000)*2
Y = np.sin(X)

"""
with above data, produce line plot similar to pyplot1.png
do NOT change the data above
hint: np.argsort
"""

I = np.argsort(X)
X = X[I]
Y = Y[I]

plt.plot(X, Y, c = 'b', label="sin")

plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.show()