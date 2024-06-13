import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from triangular_mesh.triangular_mesh_space import *

# Example usage of each function

# 1. Triangulate a function graph
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
XYZ = np.column_stack([X.flatten(), Y.flatten(), Z.flatten()])
tri_function_graph = triangulateFunctionGraph(XYZ)

# 2. Triangulate a sphere
S1, S2, S3, tri_sphere = triangulateSphere(k=30, r=2)

# 3. Triangulate an ellipsoid
A = np.array([[2, 0, 0],
              [0, 3, 0],
              [0, 0, 1]])
E1, E2, E3, tri_ellipsoid = triangulateEllipsoid(A, k=30)

# 4. Triangulate a surface defined by a function
def f(X, Y):
    return X**2 - Y**2, 2*X*Y, X + Y

S1_surf, S2_surf, S3_surf, tri_surface = triangulateSurface(f, u=(-2, 2), v=(-2, 2))

# Plotting

fig = plt.figure(figsize=(12, 12))

# Plot function graph
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_trisurf(XYZ[:, 0], XYZ[:, 1], XYZ[:, 2], triangles=tri_function_graph.simplices, cmap=cm.coolwarm)
ax1.set_title('Triangulated Function Graph')

# Plot sphere
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_trisurf(S1, S2, S3, triangles=tri_sphere.simplices, cmap=cm.coolwarm)
ax2.set_title('Triangulated Sphere')

# Plot ellipsoid
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_trisurf(E1, E2, E3, triangles=tri_ellipsoid.simplices, cmap=cm.coolwarm)
ax3.set_title('Triangulated Ellipsoid')

# Plot surface
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_trisurf(S1_surf, S2_surf, S3_surf, triangles=tri_surface.simplices, cmap=cm.coolwarm)
ax4.set_title('Triangulated Surface')

plt.tight_layout()
plt.show()
