import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mesa.space import TriangularMesh
from mesa.agent import Agent
import time

class MyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

def simulate_step(step):
    # Clear the previous plot
    ax.clear()
    ax.set_title(f"Step {step + 1}")

    # Plot mesh
    for simplex in mesh._tri.simplices:
        ax.plot_trisurf(
            points[simplex, 0], points[simplex, 1], points[simplex, 2],
            alpha=0.2, color='gray'
        )
    
    # Plot agents
    for agent in mesh._agents:
        pos = np.array(agent.pos)
        ax.scatter(pos[0], pos[1], pos[2], color='blue', marker='o')

    # Move agents randomly
    for agent in mesh._agents:
        current_pos = np.array(agent.pos)
        new_pos = current_pos + np.random.normal(size=3) * 0.5  # Random movement
        mesh.move_agent(agent, tuple(new_pos))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(True)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a TriangularMesh instance
mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# Generate a set of random points in 3D space
num_points = 20
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)

# Place agents randomly within the mesh
num_agents = 10
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)  # Pass mesh as the model
    random_point = np.random.rand(3) * 10  # Random position within the mesh
    mesh.place_agent(agent, tuple(random_point))

# Create the animation
anim = FuncAnimation(fig, simulate_step, frames=10, interval=500)

plt.show()
