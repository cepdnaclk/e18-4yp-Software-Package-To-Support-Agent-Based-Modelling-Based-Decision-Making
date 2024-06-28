import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from triangular_mesh.triangular_mesh_space import compute_surface_mesh


def generate_random_points(num_points, x_limits, y_limits, z_limits):
    # Generate random points within specified limits
    x = np.random.uniform(x_limits[0], x_limits[1], num_points)
    y = np.random.uniform(y_limits[0], y_limits[1], num_points)
    z = np.random.uniform(z_limits[0], z_limits[1], num_points)
    points = np.column_stack((x, y, z))
    return points

# Example usage
# Define limits for x, y, and z coordinates
x_limits = (0, 10)
y_limits = (0, 1)
z_limits = (0, 1)  # Limiting z between 0 and 5

# Generate random 3D coordinates as points on the surface
num_points = 6
points = generate_random_points(num_points, x_limits, y_limits, z_limits)

# Compute surface mesh
triangles = compute_surface_mesh(points)

# Visualization
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Plot triangles
for triangle in triangles:
    triangle = np.vstack((triangle, triangle[0]))  # Connect last point to first to close the triangle
    ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 'k-')

# Plot points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')

plt.show()
