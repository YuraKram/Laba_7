import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5*np.pi, 5*np.pi, 100)
y = np.cos(x)
z = np.sin(x)

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot(x, y, z, marker='.', c='red')

ax3.set_xlabel("X label")
ax3.set_ylabel("Y label")
ax3.set_zlabel("Z label")

plt.show()
