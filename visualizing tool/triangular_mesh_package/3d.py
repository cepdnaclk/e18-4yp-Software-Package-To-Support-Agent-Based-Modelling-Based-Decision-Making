import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot the triangular mesh
def plot_triangular_mesh(ax, vertices, triangles):
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], triangles, vertices[:, 2], cmap='viridis')

# Function to find neighboring triangles for each triangle
def find_neighbors(triangles):
    neighbors = [[] for _ in range(len(triangles))]
    for i, tri in enumerate(triangles):
        for j, other_tri in enumerate(triangles):
            if i != j and len(set(tri) & set(other_tri)) == 2:
                neighbors[i].append(j)
    return neighbors

# Function to simulate agent movement
def simulate_agents(vertices, triangles, neighbors, num_agents=100, steps=100):
    agents = np.random.randint(0, len(triangles), num_agents)  # Initial positions of agents
    agent_history = [agents.copy()]

    for _ in range(min(10, steps)):  # Stop after 10 steps or less if steps is less than 10
        for i, agent in enumerate(agents):
            current_height = vertices[triangles[agent]].mean(axis=0)[2]
            neighbor_heights = [vertices[triangles[n]].mean(axis=0)[2] for n in neighbors[agent]]

            # Find neighbor with lowest height
            min_neighbor_idx = np.argmin(neighbor_heights)
            min_neighbor = neighbors[agent][min_neighbor_idx]

            # Move agent to neighbor with lowest height
            if neighbor_heights[min_neighbor_idx] < current_height:
                agents[i] = min_neighbor % len(triangles)  # Ensure agent index stays within bounds

        agent_history.append(agents.copy())

    return agent_history

# Function to plot agent movement
def plot_agent_movement(ax, vertices, triangles, agent_history):
    scatter = None  # Initialize scatter object
    for step in range(10):  # Iterate over 10 steps
        agents = agent_history[step]
        ax.clear()
        plot_triangular_mesh(ax, vertices, triangles)
        if scatter is not None:
            scatter.remove()  # Remove scatter plot of agents from previous step
        # Add a small offset to the z-coordinate to place agent points above the surface
        z_offset = 0.01
        scatter = ax.scatter(vertices[triangles[agents], 0], vertices[triangles[agents], 1], vertices[triangles[agents], 2] + z_offset, color='black', zorder=10)
        ax.set_title(f"Step {step}")
        plt.pause(2)  # Pause for better visualization

# Read face data from file
def read_face(file):
    with open(file, 'r') as vertices:
        return np.array([
            [float(v) for v in line.split()]
            for line in vertices
        ])

# Load face data
xyz = read_face('face.vert')

# Create Delaunay triangulation
tri = Delaunay(xyz[:, :2])
triangles = tri.simplices

# Find neighbors for each triangle
neighbors = find_neighbors(triangles)

# Plot initial state
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111, projection='3d')
plot_triangular_mesh(ax, xyz, triangles)
plt.show()

# Simulate agent movement
agent_history = simulate_agents(xyz, triangles, neighbors, num_agents=10, steps=10)

# Plot agent movement for 10 steps
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_agent_movement(ax, xyz, triangles, agent_history)
plt.show()
