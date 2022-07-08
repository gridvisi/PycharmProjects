import matplotlib.pyplot as plt
import numpy as np
from matplotlib import figure
#Matplotlip plots of arrays
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
array1 = np.arange(-10, 10, 0.10)
array2 = np.arange(-7, 7, 0.20)
array1, array2 = np.meshgrid(array1, array2)
R = np.sqrt(array1**2 + array2**2)
Z = np.sin(R)
ax.plot_surface(array1, array2, Z, rstride=1, cstride=1,
                cmap='viridis')