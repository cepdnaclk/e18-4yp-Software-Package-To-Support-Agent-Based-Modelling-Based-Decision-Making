import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from triangular_mesh.triangular_mesh_space import *
import mesa

# 2. Triangulate a sphere
S1, S2, S3, tri_sphere = triangulateSphere(k=4, r=1)

print("...Start point...")
print(tri_sphere.simplices)
print("Length",len(tri_sphere.simplices))
print("S1:",S2)
tri_coordinates = tri_sphere.simplices
# neighbor = find_neighbors(tri_coordinates)
# print("Neigh: ",neighbor)
print(f"random: {str(tri_coordinates[np.random.choice(len(tri_coordinates))])}")

# Plot sphere
fig = plt.figure(figsize=(12, 12))