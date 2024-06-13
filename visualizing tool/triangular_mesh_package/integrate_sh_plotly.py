import numpy as np
import plotly.graph_objects as go
from mesa import Agent, Model
from mesa.time import RandomActivation
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
        new_position = self.model.project_to_surface(new_position)
        self.model.grid.move_agent(self, new_position)
        self.position = new_position


class RiverbedModel(Model):
    def __init__(self, width, height, depth, num_particles):
        super().__init__()
        self.width = width
        self.height = height
        self.depth = depth
        self.num_particles = num_particles
        self.schedule = RandomActivation(self)
        self.grid = TriangularMesh(width, height, depth, torus=False)
        self.create_mesh()

        # Create water particles
        for i in range(self.num_particles):
            pos = np.random.rand(3) * [self.width, self.height, self.depth]
            pos = self.project_to_surface(pos)
            vel = np.random.rand(3) * 0.1  # Random initial velocity
            particle = WaterParticle(i, self, pos, vel)
            self.grid.place_agent(particle, pos)
            self.schedule.add(particle)

    def create_mesh(self):
        # Generate random points in 3D space for the base surface
        points = np.random.rand(self.num_particles, 3) * [self.width, self.height, self.depth]
        self.grid.generate_delaunay_triangulation(points)

    def project_to_surface(self, position):
        # Find the triangle containing the particle
        index = self.grid.tri.find_simplex(position[:2])
        if index == -1:  # If the point is outside the convex hull, return the original position
            return position
        # Find the barycentric coordinates of the projection
        barycentric_coords = self.grid.tri.transform[index, :2].dot(position[:2] - self.grid.tri.transform[index, 2])
        # Project the point onto the triangle in 3D space
        z_coordinate = np.dot(self.grid.tri.transform[index, 2], barycentric_coords)
        projected_position = np.array([position[0], position[1], z_coordinate])
        return projected_position

    def step(self):
        self.schedule.step()
        self.visualize_particles()

    def visualize_particles(self):
        positions = np.array([agent.position for agent in self.schedule.agents])
        self.fig = go.Figure()

        # Plot mesh
        for simplex in self.grid.tri.simplices:
            x = self.grid.points[simplex, 0]
            y = self.grid.points[simplex, 1]
            z = self.grid.points[simplex, 2]
            self.fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=0.2, color='gray'))

        # Create initial agent positions
        self.fig.add_trace(go.Scatter3d(
            x=positions[:, 0],
            y=positions[:, 1],
            z=positions[:, 2],
            mode='markers',
            marker=dict(color='red', size=5),
            name='Agents'
        ))

        # Define the layout
        self.fig.update_layout(
            title="Agent Movement Animation",
            scene=dict(
                xaxis=dict(range=[0, self.width]),
                yaxis=dict(range=[0, self.height]),
                zaxis=dict(range=[0, self.depth]),
                aspectmode='cube'
            ),
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }]
        )

        # Create frames for animation
        frames = []

        for step in range(100):  # Run for 100 steps as an example
            self.schedule.step()

            # Move agents randomly
            positions = np.array([agent.position for agent in self.schedule.agents])

            # Create a frame
            frames.append(go.Frame(data=[
                go.Scatter3d(
                    x=positions[:, 0],
                    y=positions[:, 1],
                    z=positions[:, 2],
                    mode='markers',
                    marker=dict(color='red', size=5)
                )
            ], name=f'Step {step + 1}'))

        self.fig.frames = frames

        self.fig.show()


# Example usage
width = 10  # Width of the riverbed
height = 5  # Height of the riverbed
depth = 2   # Depth of the riverbed
num_particles = 100  # Number of water particles

riverbed_model = RiverbedModel(width, height, depth, num_particles)

riverbed_model.visualize_particles()
