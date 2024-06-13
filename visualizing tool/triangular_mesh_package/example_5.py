# Assuming you have already imported the necessary libraries in your Mesa model
from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
import numpy as np
from scipy.spatial import Delaunay

def triangulateSphere(k=5,r=1):
    U = np.linspace(0, 2 * np.pi, k)
    V = np.linspace(0, np.pi, k)
    [X, Y] = np.meshgrid(U, V)
    S1 = r*np.cos(X) * np.sin(Y)
    S2 = r*np.sin(X) * np.sin(Y)
    S3 = r*np.cos(Y)
    tri = Delaunay(np.array([X.flatten(), Y.flatten()]).T)
    return S1.flatten(), S2.flatten(), S3.flatten(), tri

class MyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.x, self.y, self.z, self.tri = triangulateSphere(k=5, r=1)

class MyModel(Model):
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.space = ContinuousSpace(1, 1, True)
        
        # Create agents
        for i in range(self.num_agents):
            agent = MyAgent(i, self)
            self.schedule.add(agent)
            self.space.place_agent(agent, (agent.x, agent.y))

# Example usage
model = MyModel(N=10)
for i in range(10):
    model.step()
