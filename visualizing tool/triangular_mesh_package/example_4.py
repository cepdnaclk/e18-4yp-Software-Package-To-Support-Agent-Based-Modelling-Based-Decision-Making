from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import numpy as np
from scipy.spatial import Delaunay

# Define the model class
class TriangularMeshModel(Model):
    def _init_(self, num_agents, steps, mesh_file):
        super()._init_()
        self.num_agents = num_agents
        self.steps = steps
        self.vertices = self.read_face(mesh_file)
        self.tri = Delaunay(self.vertices[:, :2])
        self.triangles = self.tri.simplices
        self.neighbors = self.find_neighbors(self.triangles)
        self.schedule = RandomActivation(self)
        
        # Create agents
        for i in range(num_agents):
            agent = Agent(i, self)
            self.schedule.add(agent)

    # Read face data from file
    def read_face(self, file):
        with open(file, 'r') as vertices:
            return np.array([
                [float(v) for v in line.split()]
                for line in vertices
            ])

    # Function to find neighboring triangles for each triangle
    def find_neighbors(self, triangles):
        neighbors = [[] for _ in range(len(triangles))]
        for i, tri in enumerate(triangles):
            for j, other_tri in enumerate(triangles):
                if i != j and len(set(tri) & set(other_tri)) == 2:
                    neighbors[i].append(j)
        return neighbors

    def step(self):
        self.schedule.step()

# Define the agent class
class Agent(Agent):
    def _init_(self, unique_id, model):
        super()._init_(unique_id, model)
        self.position = np.random.randint(0, len(model.triangles))

    def move(self):
        current_height = model.vertices[model.triangles[self.position]].mean(axis=0)[2]
        neighbor_heights = [model.vertices[model.triangles[n]].mean(axis=0)[2] for n in model.neighbors[self.position]]

        # Find neighbor with lowest height
        min_neighbor_idx = np.argmin(neighbor_heights)
        min_neighbor = model.neighbors[self.position][min_neighbor_idx]

        # Move agent to neighbor with lowest height
        if neighbor_heights[min_neighbor_idx] < current_height:
            self.position = min_neighbor % len(model.triangles)  # Ensure agent index stays within bounds

# Define visualization elements
def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}
    portrayal["x"], portrayal["y"] = model.vertices[model.triangles[agent.position], :2]
    portrayal["z"] = model.vertices[model.triangles[agent.position], 2]
    return portrayal

# Create and launch the visualization server
model_params = {
    "num_agents": 10,
    "steps": 10,
    "mesh_file": 'face.vert'
}
canvas_element = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(TriangularMeshModel,
                       [canvas_element],
                       "Triangular Mesh Model",
                       model_params)
server.port = 8521
server.launch()