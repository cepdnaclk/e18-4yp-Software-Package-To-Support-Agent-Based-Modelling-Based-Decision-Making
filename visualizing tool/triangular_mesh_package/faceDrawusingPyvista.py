import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def triangulateFunctionGraph(ax, XYZ, cmap=cm.magma):
    tri = Delaunay(XYZ[:,:2]) # triangulate projections
    ax.plot_trisurf(
        XYZ[:,0], XYZ[:,1], XYZ[:,2],
        triangles=tri.simplices, cmap=cmap
    )
    
def readFace(file):
    with open(file, 'r') as vertices:
        return np.array([
            [float(v) for v in line.split()]
            for line in vertices
        ])

xyz = readFace('face.vert')
triangulateFunctionGraph(ax, xyz)

plt.show()