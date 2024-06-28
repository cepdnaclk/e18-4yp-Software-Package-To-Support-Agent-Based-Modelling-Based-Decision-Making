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
num_points = 300
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)

# Place agents on the surface of the mesh
num_agents = 50
surface_points = mesh.get_surface_points()
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)
    random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
    random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
    mesh.place_agent(agent, random_surface_point_coords)

# Number of steps in the simulation
num_steps = 10

# Create a Plotly figure
fig = go.Figure()

# Add mesh to the initial frame
for simplex in mesh._tri.simplices:
    x = points[simplex, 0]
    y = points[simplex, 1]
    z = points[simplex, 2]
    fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=0.2, color='gray', name='Mesh'))

# Initial agent positions
agent_positions = np.array([agent.pos for agent in mesh._agents])
fig.add_trace(go.Scatter3d(
    x=agent_positions[:, 0],
    y=agent_positions[:, 1],
    z=agent_positions[:, 2],
    mode='markers',
    marker=dict(color='red', size=5),
    name='Agents'
))

# Create frames for each step
frames = []
for step in range(num_steps):
    # Move agents randomly
    for agent in mesh._agents:
        random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
        random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
        mesh.move_agent(agent, random_surface_point_coords)
    
    # Update agents' positions
    agent_positions = np.array([agent.pos for agent in mesh._agents])
    frame = go.Frame(data=[
        go.Scatter3d(
            x=agent_positions[:, 0],
            y=agent_positions[:, 1],
            z=agent_positions[:, 2],
            mode='markers',
            marker=dict(color='red', size=5),
            name='Agents'
        )
    ], name=f"frame{step+1}")
    frames.append(frame)

fig.frames = frames

# Update the layout for animation
fig.update_layout(
    title="Agent Movement on Mesh",
    scene=dict(
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 10]),
        zaxis=dict(range=[0, 10]),
        aspectmode='cube'
    ),
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[dict(label="Play",
                      method="animate",
                      args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])]
    )]
)

# Show the figure
fig.show()
