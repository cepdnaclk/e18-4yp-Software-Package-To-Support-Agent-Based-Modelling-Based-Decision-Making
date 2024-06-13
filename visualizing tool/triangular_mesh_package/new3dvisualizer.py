import numpy as np
import pyvista as pv
import time
from mesa.space import TriangularMesh
from mesa.agent import Agent

class MyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

# Create a TriangularMesh instance
mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# Generate a set of random points in 3D space
num_points = 10
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)

# Place agents on the surface of the mesh
num_agents = 10
surface_points = mesh.get_surface_points()
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)
    random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
    random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
    mesh.place_agent(agent, random_surface_point_coords)

# Create a PyVista mesh from the TriangularMesh
pv_mesh = pv.PolyData()
pv_mesh.points = points
pv_mesh.faces = mesh._tri.simplices

# Create a PyVista plotter
plotter = pv.Plotter()

# Add the mesh to the plotter
plotter.add_mesh(pv_mesh, color='gray', opacity=0.2)

# Add agents as point glyphs to the plotter
agent_positions = np.array([agent.pos for agent in mesh._agents])
plotter.add_points(agent_positions, color='red', point_size=10)

# Set up the plotter window
plotter.show(auto_close=False)

# Simulation loop
num_steps = 10
for step in range(num_steps):
    # Move agents randomly
    for agent in mesh._agents:
        random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
        random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
        mesh.move_agent(agent, random_surface_point_coords)

    # Update agent positions in PyVista plotter
    agent_positions = np.array([agent.pos for agent in mesh._agents])
    plotter.update_coordinates(agent_positions, render=False)

    # Update the plotter title
    plotter.title = f"Step {step + 1}"

    # Render the updated plotter
    plotter.show()

    # Introduce a delay to visualize movement
    time.sleep(2)  # Adjust delay time as needed
