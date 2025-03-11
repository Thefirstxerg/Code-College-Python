import numpy as np

import matplotlib.pyplot as plt

# Create data points
t = np.linspace(0, 20*np.pi, 1000)
x = t * np.cos(t)
y = t * np.sin(t)

# Create the plot
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))
scatter = ax.scatter(x, y, c=t, cmap='viridis', s=10)

# Customize the plot
ax.set_title("Spiral Galaxy", fontsize=24)
ax.set_xlabel("X Coordinate", fontsize=14)
ax.set_ylabel("Y Coordinate", fontsize=14)
ax.set_aspect('equal')

# Add a color bar
plt.colorbar(scatter, label='Time')

# Remove grid
ax.grid(False)

plt.show()