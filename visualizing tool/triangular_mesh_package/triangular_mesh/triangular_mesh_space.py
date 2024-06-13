# space.py

import numpy as np
from scipy.spatial import Delaunay
from matplotlib import cm

def triangulateFunctionGraph(XYZ):
    tri = Delaunay(XYZ[:,:2])
    return tri

# Spherical Coordinates:

# Spherical coordinates are often denoted as (r, θ, φ), where:
# r is the radial distance from the origin (center of the sphere),
# θ is the polar angle measured from the positive z-axis (ranging from 0 to π), and
# φ is the azimuthal angle measured from the positive x-axis in the xy-plane (ranging from 0 to 2π).
# These coordinates define a point on the surface of a sphere.
# Conversion to Cartesian Coordinates:

# To represent points on a sphere in Cartesian coordinates (x, y, z), we use the following formulas:
# x = r * sin(θ) * cos(φ)
# y = r * sin(θ) * sin(φ)
# z = r * cos(θ)
# Here, θ and φ are the angles we generate using U and V arrays in the code.
# These formulas convert spherical coordinates to Cartesian coordinates, giving us points on the surface of a sphere.
# Mesh Grid:

# The meshgrid function in NumPy is used to generate a grid of points from the arrays U and V.
# For each combination of values in U and V, a point is generated on the sphere using the spherical-to-Cartesian conversion formulas.
# Delaunay Triangulation:

# Delaunay triangulation is a method for creating a triangular mesh from a set of points.
# In this code, the Delaunay function from SciPy's spatial module is used to perform Delaunay triangulation on the points generated from the mesh grid.
# This generates a set of triangles that cover the surface of the sphere.
# Flattening:

# Finally, the coordinates of the points (S1, S2, S3) are flattened into 1D arrays for convenience, and the triangulation object is returned along with these flattened arrays.
def triangulateSphere(k=5,r=1):
    U = np.linspace(0, 2 * np.pi, k)
    V = np.linspace(0, np.pi, k)
    [X, Y] = np.meshgrid(U, V)
    S1 = r*np.cos(X) * np.sin(Y)
    S2 = r*np.sin(X) * np.sin(Y)
    S3 = r*np.cos(Y)
    tri = Delaunay(np.array([X.flatten(), Y.flatten()]).T)
    return S1.flatten(), S2.flatten(), S3.flatten(), tri

def triangulateEllipsoid(A, k=30):
    U = np.linspace(0, 2 * np.pi, k)
    V = np.linspace(0, np.pi, k)
    [X, Y] = np.meshgrid(U, V)
    S1 = np.cos(X) * np.sin(Y)
    S2 = np.sin(X) * np.sin(Y)
    S3 = np.cos(Y)
    E1 = np.zeros((k,k))
    E2 = np.zeros((k,k))
    E3 = np.zeros((k,k))
    for i in range(k):
        for j in range(k):
            xyz = np.array([S1[i,j], S2[i,j], S3[i,j]])
            [E1[i,j], E2[i,j], E3[i,j]] = A @ xyz
    tri = Delaunay(np.array([X.flatten(), Y.flatten()]).T)
    return E1.flatten(), E2.flatten(), E3.flatten(), tri

def triangulateSurface(f, u, v, k=30):
    U = np.linspace(*u)
    V = np.linspace(*v)
    [X, Y] = np.meshgrid(U, V)
    S1, S2, S3 = f(X, Y)  # Call the function with X and Y and unpack its return values
    tri = Delaunay(np.array([X.flatten(), Y.flatten()]).T)
    return S1.flatten(), S2.flatten(), S3.flatten(), tri

