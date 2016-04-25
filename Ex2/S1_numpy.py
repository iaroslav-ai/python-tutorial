import numpy as np
import matplotlib.pyplot as plt
from backend import show_tensor

z = np.zeros((12,12))
z2 = np.zeros((1,12))
z2[0,::2] = 1.0

z3 = np.copy(z)

I = [1,3,5,6]

z3[I,I] = 1.0

show_tensor([z3])