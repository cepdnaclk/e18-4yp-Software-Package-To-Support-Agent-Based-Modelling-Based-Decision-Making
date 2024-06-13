import numpy as np
import plotly.graph_objects as go
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
mesh.generate_delaunay_triangulation(points)

# Place agents on the surface of the mesh
num_agents = 10
surface_points = mesh.get_surface_points()
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)
    random_surface_point_index = np.random.choice(range(len(surface_points)))
    random_surface_point_coords = surface_points[random_surface_point_index]
    mesh.place_agent(agent, random_surface_point_coords)

# Visualize using Plotly
fig = go.Figure()

# Plot mesh triangles
for simplex in mesh._tri.simplices:
    x_coords = points[simplex, 0]
    y_coords = points[simplex, 1]
    z_coords = points[simplex, 2]
    fig.add_trace(go.Mesh3d(x=x_coords, y=y_coords, z=z_coords, opacity=0.2, color='gray'))

# Plot agents
for agent in mesh._agents:
    pos = np.array(agent.pos)
    fig.add_trace(go.Scatter3d(x=[pos[0]], y=[pos[1]], z=[pos[2]], mode='markers', marker=dict(size=5, color='red')))

# Update layout
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
        aspectmode='data'
    )
)

# Show the Plotly figure
fig.show()
