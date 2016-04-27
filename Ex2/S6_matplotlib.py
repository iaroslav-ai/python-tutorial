import numpy as np
import matplotlib.pyplot as plt


# 2d array: matrix
X = np.linspace(0, 3, 100)

#plt.scatter(X, np.exp(X))
#plt.show()

# point plot
plt.scatter(X, np.exp(X), c = 'r', label="exp")

# line plot
plt.plot(X, np.sin(X), c = 'b', label="sin")

plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.show()