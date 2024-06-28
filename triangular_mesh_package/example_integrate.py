import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from triangular_mesh.triangular_mesh_space import *
import mesa


# # Function to find neighboring triangles for each triangle
# def find_neighbors(triangles):
#     neighbors = [[] for _ in range(len(triangles))]
#     for i, tri in enumerate(triangles):
#         for j, other_tri in enumerate(triangles):
#             if i != j and len(set(tri) & set(other_tri)) == 2:
#                 neighbors[i].append(j)
#     return neighbors

# # 2. Triangulate a sphere
# S1, S2, S3, tri_sphere = triangulateSphere(k=4, r=1)

# print("...Start point...")
# print(tri_sphere.simplices)
# print("Length",len(tri_sphere.simplices))
# tri_coordinates = tri_sphere.simplices
# neighbor = find_neighbors(tri_coordinates)
# print("Neigh: ",neighbor)
# print(f"random: {str(tri_coordinates[np.random.choice(len(tri_coordinates))])}")

# # Plot sphere
# fig = plt.figure(figsize=(12, 12))

# ax2 = fig.add_subplot(222, projection='3d')
# ax2.plot_trisurf(S1, S2, S3, triangles=tri_sphere.simplices, cmap=cm.coolwarm)
# ax2.set_title('Triangulated Sphere')

# # Label each triangle with its index
# # for i, triangle in enumerate(tri_sphere.simplices):
# #     # Calculate centroid of the triangle
# #     centroid = np.mean([np.array([S1[idx], S2[idx], S3[idx]]) for idx in triangle], axis=0)
# #     ax2.text(centroid[0], centroid[1], centroid[2], str(i), color='black')

# # Label each point with its index
# all_vertices = set(tri_sphere.simplices.flatten())  # Get all unique vertex indices
# # print(f"vertices: {str(all_vertices)}")
# for idx in all_vertices:
#     ax2.text(S1[idx], S2[idx], S3[idx], str(idx), color='black')

# plt.tight_layout()
# plt.show()


# #---------------------------------------------------------------------------------------------------------------------------

# class SphereAgent(mesa.Agent):
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         # self.position = position
#         self.wealth = 1

#     # def move(self):
#     #     # Implement movement logic here (e.g., random walk on the sphere)
#     #     # Example: Randomly select a neighboring vertex
#     #     neighbors = self.model.get_neighbors(self.position)
#     #     new_position = self.random.choice(neighbors)
#     #     self.position = new_position

#     # def give_money(self):
#     #     # Implement interaction logic here (e.g., give money to neighboring agents)
#     #     # Example: Give money to a neighboring agent
#     #     cellmates = self.model.grid.get_cell_list_contents([self.position])
#     #     if len(cellmates) > 1:
#     #         other_agent = self.random.choice(cellmates)
#     #         other_agent.wealth += 1
#     #         self.wealth -= 1

#     # def step(self):
#     #     print(f"Hi, I am an agent, you can call me {str(self.unique_id)}. and my wealth is {str(self.wealth)}")
#         # self.move()
#         # if self.wealth > 0:
#         #     self.give_money()
#     def step(self):
#         # Verify agent has some wealth
#         if self.wealth > 0:
#             other_agent = self.random.choice(self.model.schedule.agents)
#             if other_agent is not None:
#                 # print(f"OtherAgent {str(other_agent.unique_id)} and Wealth {str(other_agent.wealth)}")
#                 # print(f"Agent {str(self.unique_id)} and Wealth {str(self.wealth)}")
#                 other_agent.wealth += 1
#                 self.wealth -= 1
#                 # print(f"OtherAgent {str(other_agent.unique_id)} and Wealth {str(other_agent.wealth)}")
#                 # print(f"Agent {str(self.unique_id)} and Wealth {str(self.wealth)}")
#         # print(f"Hi, I am an agent, you can call me {str(self.unique_id)}. and my wealth is {str(self.wealth)}")


# class SphereModel(mesa.Model):
#     def __init__(self, N):
#         super().__init__()
#         # self.vertices = vertices
#         # self.simplices = simplices
#         self.num_agents = N
#         # self.grid = mesa.space.NetworkGrid(self.vertices, self.simplices)
#         self.schedule = mesa.time.RandomActivation(self)
#         # Create agents
#         for i in range(self.num_agents):
#             a = SphereAgent(i, self)  # Initialize agents at vertex i
#             self.schedule.add(a)

#     # def get_neighbors(self, position):
#     #     # Return neighboring vertices for a given position (vertex index)
#     #     return self.grid.get_neighbors(position)

#     def step(self):
#         self.schedule.step()

# print("Test")
# starter_model = SphereModel(10)
# starter_model.step()

# # Assuming you have the vertices (S1, S2, S3) and simplices (tri_sphere.simplices)
# # Create the model
# # model = SphereModel(vertices=list(range(len(S1))), simplices=tri_sphere.simplices)

# # # Run the model for some number of steps
# # for _ in range(10):
# #     model.step()

# # # Example: Plot the sphere
# # fig = plt.figure(figsize=(12, 12))
# # ax = fig.add_subplot(111, projection='3d')
# # ax.plot_trisurf(S1, S2, S3, triangles=tri_sphere.simplices, cmap=cm.coolwarm)
# # plt.show()

# #-----------------------------------------------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mesa
from mesa.space import NetworkGrid
from mesa.time import RandomActivation

class TriangularAgent(mesa.Agent):
    def __init__(self, unique_id, model, triangle_index):
        super().__init__(unique_id, model)
        self.triangle_index = triangle_index

    def step(self):
        neighbors = self.model.get_neighbors(self.triangle_index)
        if neighbors:
            new_triangle_index = np.random.choice(neighbors)
            self.model.move_agent(self, new_triangle_index)


class TriangularModel(mesa.Model):
    def __init__(self, simplices):
        super().__init__()
        # self.vertices = N
        self.simplices = simplices
        self.num_agents = len(simplices)
        # self.grid = NetworkGrid(list(range(len(vertices))), simplices)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = TriangularAgent(i, self, i)  # Initialize agents on triangles
            self.schedule.add(a)
            self.grid.place_agent(a, i)  # Place agent on triangle i

    def get_neighbors(self, triangle_index):
        # Return neighboring triangles for a given triangle index
        neighbors = []
        for simplex in self.simplices:
            if triangle_index in simplex:
                neighbors.extend(simplex)
        neighbors.remove(triangle_index)  # Remove the current triangle itself
        return neighbors

    def move_agent(self, agent, new_triangle_index):
        self.grid.move_agent(agent, new_triangle_index)

    def step(self):
        self.schedule.step()


# Assuming you have S1, S2, S3, and tri_sphere defined
# You can use the following code to create and run the model
        
        # 2. Triangulate a sphere
S1, S2, S3, tri_sphere = triangulateSphere(k=4, r=1)

# print("...Start point...")
# print(tri_sphere.simplices)
# print("Length",len(tri_sphere.simplices))
# tri_coordinates = tri_sphere.simplices
# neighbor = find_neighbors(tri_coordinates)
# print("Neigh: ",neighbor)
# print(f"random: {str(tri_coordinates[np.random.choice(len(tri_coordinates))])}")

# # Plot sphere
# fig = plt.figure(figsize=(12, 12))

# ax2 = fig.add_subplot(222, projection='3d')
# ax2.plot_trisurf(S1, S2, S3, triangles=tri_sphere.simplices, cmap=cm.coolwarm)
# ax2.set_title('Triangulated Sphere')

# Create and visualize the model
tri_model = TriangularModel(tri_sphere.simplices)

# Run the model for a certain number of steps
for _ in range(100):
    tri_model.step()

# Visualize the updated positions of agents or any other post-processing
