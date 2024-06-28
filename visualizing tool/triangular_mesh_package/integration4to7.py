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

# Move agents within the mesh
num_steps = 10

# Create a Plotly figure
fig = go.Figure()

for step in range(num_steps):
    # Clear previous traces
    fig.data = []

    # Plot mesh
    for simplex in mesh._tri.simplices:
        x = points[simplex, 0]
        y = points[simplex, 1]
        z = points[simplex, 2]
        fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=0.2, color='gray'))

    # Plot agents
    agent_positions = np.array([agent.pos for agent in mesh._agents])
    fig.add_trace(go.Scatter3d(
        x=agent_positions[:, 0],
        y=agent_positions[:, 1],
        z=agent_positions[:, 2],
        mode='markers',
        marker=dict(color='red', size=5)
    ))

    # Move agents randomly
    for agent in mesh._agents:
        random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
        random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
        mesh.move_agent(agent, random_surface_point_coords)

    # Update the layout
    fig.update_layout(
        title=f"Step {step + 1}",
        scene=dict(
            xaxis=dict(range=[0, 10]),
            yaxis=dict(range=[0, 10]),
            zaxis=dict(range=[0, 10]),
            aspectmode='cube'
        )
    )

    # Pause between steps (optional)
    # You can adjust the pause time by changing the value of 'pause_duration' (in seconds)
    pause_duration = 0.5
    fig.show()
    fig.update_traces(visible=False)
    fig.data = []

# ==========================================================================================================================

# import numpy as np
# import plotly.graph_objects as go
# import time
# from mesa.space import TriangularMesh
# from mesa.agent import Agent

# class MyAgent(Agent):
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)

# # Create a TriangularMesh instance
# mesh = TriangularMesh(x_max=10, y_max=10, z_max=10, torus=False)

# # Generate a set of random points in 3D space
# num_points = 100
# points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube

# # Generate Delaunay triangulation based on the random points
# mesh.generate_delaunay_triangulation(points)

# # Place agents on the surface of the mesh
# num_agents = 30
# surface_points = mesh.get_surface_points()
# for i in range(num_agents):
#     agent = MyAgent(unique_id=i, model=mesh)
#     random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
#     random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
#     mesh.place_agent(agent, random_surface_point_coords)

# # Initialize the Plotly figure
# fig = go.Figure()

# # Plot mesh (static plot, won't change)
# for simplex in mesh._tri.simplices:
#     x = points[simplex, 0]
#     y = points[simplex, 1]
#     z = points[simplex, 2]
#     fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=0.2, color='gray'))

# # Plot agents (initial positions)
# agent_positions = np.array([agent.pos for agent in mesh._agents])
# agents_trace = go.Scatter3d(
#     x=agent_positions[:, 0],
#     y=agent_positions[:, 1],
#     z=agent_positions[:, 2],
#     mode='markers',
#     marker=dict(color='red', size=5)
# )
# fig.add_trace(agents_trace)

# # Update layout
# fig.update_layout(
#     title="Step 0",
#     scene=dict(
#         xaxis=dict(range=[0, 10]),
#         yaxis=dict(range=[0, 10]),
#         zaxis=dict(range=[0, 10]),
#         aspectmode='cube'
#     )
# )

# # Display the initial state of the simulation
# fig.show()

# # Simulation loop
# num_steps = 10
# for step in range(1, num_steps + 1):
#     # Move agents randomly
#     for agent in mesh._agents:
#         random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
#         random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
#         mesh.move_agent(agent, random_surface_point_coords)

#     # Update agents' positions
#     agent_positions = np.array([agent.pos for agent in mesh._agents])
#     agents_trace.x = agent_positions[:, 0]
#     agents_trace.y = agent_positions[:, 1]
#     agents_trace.z = agent_positions[:, 2]

#     # Update layout title
#     fig.update_layout(title=f"Step {step}")

#     # Display the updated Plotly figure
#     fig.show()

#     # Introduce 2-second delay to visualize movement
#     time.sleep(2)  # Adjust delay time as needed
