import time
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt


class WaterParticle(Agent):
    def __init__(self, unique_id, model, position, velocity):
        super().__init__(unique_id, model)
        self.position = position
        self.velocity = velocity

    def step(self):
        # Gravity
        gravity = np.array([0, -0.1])  # Example gravity vector, adjust as needed
        # Viscosity
        viscosity_coefficient = 0.01  # Adjust as needed
        # Pressure gradients
        # Example pressure gradient calculation (replace with actual calculation)
        dP_dx = 0.01  # Example pressure gradient in the x-direction
        dP_dy = 0.01  # Example pressure gradient in the y-direction

        # Update position based on velocity
        new_position = self.position + self.velocity
        # Apply gravity
        new_position += gravity
        # Apply viscosity
        viscosity_force = -viscosity_coefficient * self.velocity
        new_position += viscosity_force
        # Apply pressure gradients
        pressure_gradient = np.array([dP_dx, dP_dy])
        pressure_force = -pressure_gradient
        new_position += pressure_force

        # Project the particle onto the surface defined by the Delaunay triangulation
        projected_position = self.project_to_surface(new_position)
        # Ensure particles stay within the bounds of the mesh
        projected_position[0] = min(max(projected_position[0], 0), self.model.width)
        projected_position[1] = min(max(projected_position[1], 0), self.model.height)
        new_position_int = (int(projected_position[0]), int(projected_position[1]))  # Convert to integers
        # Move the particle to the new position
        self.model.grid.move_agent(self, new_position_int)
        self.position = projected_position

    def project_to_surface(self, position):
        # Find the triangle containing the particle
        index = self.model.tri.find_simplex(position)
        if index == -1:  # If the point is outside the convex hull, return the original position
            return position
        # Find the barycentric coordinates of the projection
        barycentric_coords = self.model.tri.transform[index, :2].dot(position - self.model.tri.transform[index, 2])
        # Project the point onto the triangle
        projected_position = np.dot(self.model.tri.transform[index, :2].T, barycentric_coords) + self.model.tri.transform[index, 2]
        return projected_position


class RiverbedModel(Model):
    def __init__(self, width, height, num_particles):
        self.width = width
        self.height = height
        self.num_particles = num_particles
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, True)  # True for toroidal grid
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.create_mesh()

        # Create water particles
        for i in range(self.num_particles):
            pos = np.random.rand(2) * [self.width, self.height]
            # Convert position array to tuple of integers for grid placement
            pos = tuple(pos.astype(int))
            vel = np.random.rand(2) * 0.1  # Random initial velocity
            particle = WaterParticle(i, self, pos, vel)
            self.grid.place_agent(particle, pos)
            self.schedule.add(particle)

        self.running = True

    def create_mesh(self):
        # Create a grid of points for the base flat surface
        x_points = np.linspace(0, self.width, int(np.sqrt(self.num_particles)))
        y_points = np.linspace(0, self.height, int(np.sqrt(self.num_particles)))
        xx, yy = np.meshgrid(x_points, y_points)
        self.points = np.vstack((xx.ravel(), yy.ravel())).T

        # Add random perturbations to create irregularities
        perturbations = np.random.normal(0, 0.9, self.points.shape)
        self.points += perturbations

        # Perform Delaunay triangulation
        self.tri = Delaunay(self.points)

    def step(self):
        self.schedule.step()
        self.visualize_particles()
        time.sleep(1)  # Pause for 1 second


    def visualize_particles(self):
        self.ax.clear()
        self.ax.plot_trisurf(self.points[:, 0], self.points[:, 1], np.zeros_like(self.points[:, 0]), triangles=self.tri.simplices.copy(), cmap='viridis', edgecolor='none', alpha = 0.6)
        positions = np.array([agent.position for agent in self.schedule.agents])
        self.ax.scatter(positions[:, 0], positions[:, 1], np.zeros_like(positions[:, 0]), color='red', s=20)  # Plot particle positions
        self.ax.set_title(f'Particles in Mesh - Step {self.schedule.steps}')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        plt.pause(0.01)  # Pause to allow the plot to update



# Example usage
width = 10  # Width of the riverbed
height = 5  # Height of the riverbed
num_particles = 100  # Number of water particles

riverbed_model = RiverbedModel(width, height, num_particles)

for _ in range(100):  # Run for 10 steps as an example
    riverbed_model.step()
