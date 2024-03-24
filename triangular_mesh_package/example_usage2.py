import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay

def generate_cuboid_points(corner_points):
    # Generate points for a cuboid given its corner points
    x_min, x_max = corner_points[0][0], corner_points[1][0]
    y_min, y_max = corner_points[0][1], corner_points[3][1]
    z_min, z_max = corner_points[0][2], corner_points[4][2]

    x = np.linspace(x_min, x_max, 2)
    y = np.linspace(y_min, y_max, 2)
    z = np.linspace(z_min, z_max, 2)

    xx, yy, zz = np.meshgrid(x, y, z)

    points = np.array([xx.flatten(), yy.flatten(), zz.flatten()]).T

    return points

# Example usage
# Define corner points for the cuboid
corner_points = np.array([
    [0, 0, 0],  # Front bottom left
    [1, 0, 0],  # Front bottom right
    [1, 1, 0],  # Front top right
    [0, 1, 0],  # Front top left
    [0, 0, 1],  # Back bottom left
    [1, 0, 1],  # Back bottom right
    [1, 1, 1],  # Back top right
    [0, 1, 1]   # Back top left
])

# Generate cuboid points
points = generate_cuboid_points(corner_points)

# Compute Delaunay triangulation
tri = Delaunay(points)

# Extract triangles
triangles = points[tri.simplices]

# Calculate triangle centroids
centroids = np.mean(triangles, axis=1)

# Assign colors based on Z coordinate of centroids
colors = centroids[:, 2]

# Visualization
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Plot triangles with colors
for i, triangle in enumerate(triangles):
    triangle = np.vstack((triangle, triangle[0]))  # Connect last point to first to close the triangle
    ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], color=plt.cm.viridis(colors[i]))

# Plot points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
sm.set_array(colors)
fig.colorbar(sm, ax=ax)

plt.show()
