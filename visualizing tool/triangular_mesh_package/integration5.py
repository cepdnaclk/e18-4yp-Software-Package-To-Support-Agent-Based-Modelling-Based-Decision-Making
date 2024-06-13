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
num_points = 10
points = np.random.rand(num_points, 3) * 10  # Random points within a 10x10x10 cube
# points = np.loadtxt('face.vert')
print("PP:",points)

# Generate Delaunay triangulation based on the random points
mesh.generate_delaunay_triangulation(points)


# Place agents on the surface of the mesh
num_agents = 10
surface_points = mesh.get_surface_points()
print("0Index Point: ",mesh.get_points_on_triangle(0))
print("3Index Point: ",mesh.get_points_on_triangle(3))
print("Length of surface_points:",len(surface_points))
print("Surface Points: ",surface_points)
No_of_simplices = len(mesh._tri.simplices)
for j in range(No_of_simplices):
    print(f"{j}th Triangle: {mesh.get_points_on_triangle(j)}")
for i in range(num_agents):
    agent = MyAgent(unique_id=i, model=mesh)
    random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
    random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
    mesh.place_agent(agent, random_surface_point_coords)

# for i in range(num_agents):
#     agent = MyAgent(unique_id=i, model=mesh)  # Create agent instance
#     random_surface_point_index = np.random.choice(range(len(surface_points)))  # Random index
#     random_surface_point_coords = surface_points[random_surface_point_index]  # Extract coordinates
#     mesh.place_agent(agent, random_surface_point_coords)  # Place agent at random surface point

#     # Check and move agent to a neighboring point if z-coordinate condition is met
#     current_pos = agent.pos
#     neighbors = mesh.find_neighboring_points(current_pos)
#     for neighbor_pos in neighbors:
#         if neighbor_pos[2] < current_pos[2]:  # Check z-coordinate of neighbor
#             print("Neighbor:",neighbor_pos)
#             print("Current:",current_pos)
#             mesh.place_agent(agent, neighbor_pos)  # Move agent to neighboring point
#             break  # Move only once based on the first eligible neighbor

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

    # # Move agents randomly
    # for agent in mesh._agents:
    #     random_surface_point = np.random.choice(range(len(surface_points)))  # Random index
    #     random_surface_point_coords = surface_points[random_surface_point]  # Extract coordinates
    #     mesh.move_agent(agent, tuple(random_surface_point_coords))

for agent in mesh._agents:
    current_pos = agent.pos
    neighbors = mesh.find_neighboring_points(current_pos)

    # Filter neighbors to find those with lower z-coordinates
    eligible_neighbors = [neighbor for neighbor in neighbors if neighbor[2] < current_pos[2]]

    # if eligible_neighbors:
    #     # Randomly select one eligible neighbor to move to
    #     chosen_neighbor = np.random.choice(eligible_neighbors)
    #     mesh.move_agent(agent, chosen_neighbor)
    print("Agent",agent.unique_id)
    print("AgentPos:",current_pos)
    print(neighbors)
    print("EN:",eligible_neighbors)
    
    # if eligible_neighbors:
    #     # Extract coordinates of eligible neighbors
    #     eligible_neighbor_coords = [neighbor for neighbor in eligible_neighbors]
    #     # Randomly select one eligible neighbor to move to
    #     chosen_neighbor_coords = np.random.choice(eligible_neighbor_coords)
    #     mesh.move_agent(agent, tuple(chosen_neighbor_coords))

    plt.pause(2)  # Pause for 1 second between steps

plt.show()  # Show the final plot window after all steps
