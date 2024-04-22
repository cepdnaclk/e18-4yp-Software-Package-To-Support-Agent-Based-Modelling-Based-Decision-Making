import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay
import timeit

def triangulate_with_delaunay(XYZ, ax, cmap=cm.magma):
    tri = Delaunay(XYZ[:,:2])
    ax.plot_trisurf(
        XYZ[:,0], XYZ[:,1], XYZ[:,2],
        triangles=tri.simplices, cmap=cmap
    )

def triangulate_with_flip_algorithm(XYZ, ax, cmap=cm.magma):
    triangles = flip_algorithm_triangulation(XYZ)
    for triangle in triangles:
        ax.plot_trisurf(
            triangle[:, 0], triangle[:, 1], triangle[:, 2],
            triangles=[[0, 1, 2]], cmap=cmap
        )

def readFace(file):
    with open(file, 'r') as vertices:
        return np.array([
            [float(v) for v in line.split()]
            for line in vertices
        ])

def is_delaunay(triangle):
    A = triangle[0]
    B = triangle[1]
    C = triangle[2]
    
    AB = B - A
    AC = C - A
    BC = C - B
    
    angle_AB = np.arccos(np.dot(AB, AC) / (np.linalg.norm(AB) * np.linalg.norm(AC)))
    angle_BC = np.arccos(np.dot(-AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))
    
    return angle_AB + angle_BC < np.pi

def flip_algorithm_triangulation(vertices):
    tri = Delaunay(vertices[:, :2])
    triangles = vertices[tri.simplices]
    
    while True:
        found = False
        for i in range(len(triangles)):
            for j in range(i + 1, len(triangles)):
                triangle1 = triangles[i]
                triangle2 = triangles[j]
                
                common_edge = np.intersect1d(triangle1, triangle2)
                if len(common_edge) == 2:
                    other_points = np.setdiff1d(np.concatenate((triangle1, triangle2)), common_edge)
                    if len(other_points) == 2:
                        quadrilateral = np.concatenate((common_edge, other_points))
                        if not is_delaunay(quadrilateral):
                            triangles[i] = np.array([common_edge[0], other_points[0], common_edge[1]])
                            triangles[j] = np.array([common_edge[1], other_points[1], common_edge[0]])
                            found = True
                            break
            if found:
                break
        if not found:
            break
    
    return triangles

def compare_execution_time():
    xyz = readFace('face.vert')
    
    # Measure time for Delaunay triangulation
    delaunay_time = timeit.timeit(
        lambda: triangulate_with_delaunay(xyz, ax),
        number=1
    )
    
    # Measure time for Flip algorithm triangulation
    flip_algorithm_time = timeit.timeit(
        lambda: triangulate_with_flip_algorithm(xyz, ax),
        number=1
    )

    print("Execution time for Delaunay triangulation:", delaunay_time, "seconds")
    print("Execution time for Flip algorithm triangulation:", flip_algorithm_time, "seconds")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
compare_execution_time()
plt.show()
