import time
import numpy as np
import matplotlib.pyplot as plt
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from scipy.spatial import Delaunay
from mesa.space import TriangularMesh

class WaterParticle(Agent):
    def __init__(self, unique_id, model, position, velocity):
        super().__init__(unique_id, model)
        self.position = position
        self.velocity = velocity

    def step(self):
        # Constants for physics simulation
        gravity = np.array([0, 0, -0.1])  # Gravity vector (x, y, z)
        viscosity_coefficient = 0.01  # Viscosity coefficient
        dP_dx = 0.01  # Pressure gradient in the x-direction
        dP_dy = 0.01  # Pressure gradient in the y-direction

        # Update position based on velocity
        new_position = self.position + self.velocity

        # Apply forces
        new_position += gravity
        viscosity_force = -viscosity_coefficient * self.velocity
        new_position += viscosity_force
        pressure_gradient = np.array([dP_dx, dP_dy, 0])  # Z-component of pressure gradient is 0
        pressure_force = -pressure_gradient
        new_position += pressure_force

        # Move the particle to the new position
        self.model.grid.move_agent(self, new_position)
        self.position = new_position

    def project_to_surface(self, position):
        # Find the triangle containing the particle
        index = self.model.tri.find_simplex(position[:2])
        if index == -1:  # If the point is outside the convex hull, return the original position
            return position
        # Find the barycentric coordinates of the projection
        barycentric_coords = self.model.tri.transform[index, :2].dot(position[:2] - self.model.tri.transform[index, 2])
        # Project the point onto the triangle in 3D space
        z_coordinate = np.dot(self.model.tri.transform[index, 2], barycentric_coords)
        projected_position = np.array([position[0], position[1], z_coordinate])
        return projected_position


class RiverbedModel(Model):
    def __init__(self, width, height, depth, num_particles):
        super().__init__()
        self.width = width
        self.height = height
        self.depth = depth
        self.num_particles = num_particles
        self.schedule = RandomActivation(self)
        self.grid = TriangularMesh(self.width, self.height, self.depth, torus=False)  # Use tuple for grid dimensions
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.create_mesh()

        # Create water particles
        for i in range(self.num_particles):
            pos = np.random.rand(3) * [self.width, self.height, self.depth]
            vel = np.random.rand(3) * 0.1  # Random initial velocity
            particle = WaterParticle(i, self, pos, vel)
            self.grid.place_agent(particle, pos)
            self.schedule.add(particle)

    def create_mesh(self):
        # Generate random points in 3D space for the base surface
        self.points = np.random.rand(self.num_particles, 3) * [self.width, self.height, self.depth]

        # Perform Delaunay triangulation
        self.tri = Delaunay(self.points[:, :2])  # Triangulate using only (x, y) coordinates

    def step(self):
        self.schedule.step()
        self.visualize_particles()
        plt.pause(0.01)

    def visualize_particles(self):
        self.ax.clear()
        self.ax.plot_trisurf(self.points[:, 0], self.points[:, 1], self.points[:, 2],
                             triangles=self.tri.simplices.copy(), cmap='viridis', edgecolor='none', alpha=0.6)
        positions = np.array([agent.position for agent in self.schedule.agents])
        self.ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], color='red', s=20)
        self.ax.set_title(f'Particles in 3D Mesh - Step {self.schedule.steps}')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')



# Example usage
width = 10  # Width of the riverbed
height = 5  # Height of the riverbed
depth = 2   # Depth of the riverbed
num_particles = 100  # Number of water particles

riverbed_model = RiverbedModel(width, height, depth, num_particles)

for _ in range(100):  # Run for 100 steps as an example
    riverbed_model.step()

plt.show()
