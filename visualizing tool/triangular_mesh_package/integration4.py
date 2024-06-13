import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mesa.space import TriangularMesh
from mesa.agent import Agent

class MyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

# Create a TriangularMesh instance
mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# Generate a set of random points in 3D space
num_points = 300
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube
# points = np.loadtxt('face.vert')
# print("PP:",points)

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)

# Place agents on the surface of the mesh
num_agents = 50
surface_points = mesh.get_surface_points()
print("Surface Points:",surface_points)
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)
    random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
    random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
    mesh.place_agent(agent, random_surface_point_coords)

# Move agents within the mesh
num_steps = 10
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.grid(True)

for step in range(num_steps):
    ax.clear()
    plt.title(f"Step {step + 1}")

    # # Plot mesh
    for simplex in mesh._tri.simplices:
        ax.plot_trisurf(
            points[simplex, 0], points[simplex, 1], points[simplex, 2],
            alpha=0.2, color='gray'
        )

    # Plot agents
    for agent in mesh._agents:
        pos = np.array(agent.pos)
        ax.scatter(pos[0], pos[1], pos[2], color='red', marker='o')

    # Move agents randomly
    for agent in mesh._agents:
        random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
        random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
        mesh.move_agent(agent, tuple(random_surface_point_coords))

    plt.pause(0.5)  # Pause for 1 second between steps

plt.show()  # Show the final plot window after all steps
