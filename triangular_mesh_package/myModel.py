import numpy as np
import plotly.graph_objects as go
from mesa import Agent, Model
from mesa.time import RandomActivation
from scipy.spatial import Delaunay

#meshspace from space.py
class MeshSpace:
    def __init__(self, vertices):
        self.vertices = vertices
        self.tri = Delaunay(self.vertices[:, :2])
        self.triangles = self.tri.simplices
        self.neighbors = self.find_neighbors(self.triangles)

    def find_neighbors(self, triangles):
        neighbors = [[] for _ in range(len(triangles))]
        for i, tri in enumerate(triangles):
            for j, other_tri in enumerate(triangles):
                if i != j and len(set(tri) & set(other_tri)) == 2:
                    neighbors[i].append(j)
        return neighbors
    
    def plot_agent_movement(vertices, triangles, agent_history):
        mesh = plot_triangular_mesh(vertices, triangles)
        frames = []
        steps = []

        for step, agents in enumerate(agent_history):
            agent_positions = vertices[triangles[agents].flatten()].reshape(-1, 3) + [0, 0, 0.01]
            scatter = go.Scatter3d(
                x=agent_positions[:, 0],
                y=agent_positions[:, 1],
                z=agent_positions[:, 2],
                mode='markers',
                marker=dict(size=5, color='black'),
                name='Agents'
            )
            frames.append(go.Frame(data=[mesh, scatter], name=str(step)))
            steps.append({
                'args': [[str(step)], {'frame': {'duration': 500, 'redraw': True}, 'mode': 'immediate'}],
                'label': str(step),
                'method': 'animate'
            })

        fig = go.Figure(data=[mesh, frames[0].data[1]], frames=frames)
        fig.update_layout(
            updatemenus=[{
                'buttons': [
                    {'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}], 'label': 'Play', 'method': 'animate'},
                    {'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}], 'label': 'Pause', 'method': 'animate'}
                ],
                'showactive': False,
                'type': 'buttons'
            }],
            sliders=[{
                'steps': steps,
                'currentvalue': {'prefix': 'Step: '}
            }]
        )
        fig.show()
    
# Visualization Functions
def plot_triangular_mesh(vertices, triangles):
    mesh = go.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=triangles[:, 0],
        j=triangles[:, 1],
        k=triangles[:, 2],
        color='lightblue',
        opacity=0.50,
        name='Mesh'
    )
    return mesh

# Define the Agent Class
class MeshAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.position = None

    def step(self):
        # Simulate agent movement
        current_triangle = self.model.space.triangles[self.position]
        current_height = self.model.space.vertices[current_triangle].mean(axis=0)[2]
        neighbor_heights = [self.model.space.vertices[self.model.space.triangles[n]].mean(axis=0)[2] for n in self.model.space.neighbors[self.position]]

        # Find neighbor with lowest height
        min_neighbor_idx = np.argmin(neighbor_heights)
        min_neighbor = self.model.space.neighbors[self.position][min_neighbor_idx]

        # Move agent to neighbor with lowest height
        if neighbor_heights[min_neighbor_idx] < current_height:
            self.position = min_neighbor % len(self.model.space.triangles)  # Ensure agent index stays within bounds

# Define the Model Class
class MeshModel(Model):
    def __init__(self, num_agents, vertex_file):
        super().__init__()
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        
        # Load vertex data
        self.vertices = self.read_face(vertex_file)
        self.space = MeshSpace(self.vertices)

        # Create agents
        for i in range(self.num_agents):
            agent = MeshAgent(i, self)
            self.schedule.add(agent)
            # Randomly place agents on triangles
            agent.position = np.random.randint(0, len(self.space.triangles))

    def step(self):
        self.schedule.step()

    def read_face(self, file):
        with open(file, 'r') as vertices:
            return np.array([[float(v) for v in line.split()] for line in vertices])


# Running the Model
if __name__ == "__main__":
    # Define the number of agents and steps
    num_agents = 20
    steps = 10

    # Load the vertex data file (replace 'face.vert' with the actual path to your file)
    vertex_file = "C:\\Users\\jfaar\\Downloads\\terrain.vert"

    # Create the model and run the simulation
    model = MeshModel(num_agents, vertex_file)

    agent_history = []
    for i in range(steps):
        model.step()
        agent_positions = [agent.position for agent in model.schedule.agents]
        agent_history.append(agent_positions)

    # Plot the agent movement
    MeshSpace.plot_agent_movement(model.vertices, model.space.triangles, agent_history)