import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)


X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Set the axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
