def find_point_neighbors(triangles):
    point_to_triangles = {}

    # Step 1: Populate point_to_triangles dictionary
    for i, triangle in enumerate(triangles):
        for point in triangle:
            point_tuple = tuple(point)
            if point_tuple not in point_to_triangles:
                point_to_triangles[point_tuple] = set()
            point_to_triangles[point_tuple].add(i)

    # Step 2: Determine neighbors for each point
    point_neighbors = {}

    for point_tuple, triangle_set in point_to_triangles.items():
        neighbors = set()
        for triangle_index in triangle_set:
            for other_point in triangles[triangle_index]:
                if tuple(other_point) != point_tuple:
                    neighbors.add(tuple(other_point))
        point_neighbors[point_tuple] = neighbors

    return point_neighbors

# Example usage with your provided triangles data
triangles = [
    [[7.18037742, 2.82816052, 6.12707099], [1.70216525, 0.81034318, 6.73663282], [5.3103598 , 8.31224183, 9.77094529], [0.60816707, 3.30868089, 7.02751862]],
    [[7.18037742, 2.82816052, 6.12707099], [1.59671011, 7.41260264, 8.15749125], [5.3103598 , 8.31224183, 9.77094529], [0.60816707, 3.30868089, 7.02751862]],
    [[7.5328052 , 5.42512004, 5.80712102], [1.59671011, 7.41260264, 8.15749125], [8.86269454, 6.12422312, 5.03115589], [0.60816707, 3.30868089, 7.02751862]],
    [[7.5328052 , 5.42512004, 5.80712102], [7.18037742, 2.82816052, 6.12707099], [1.59671011, 7.41260264, 8.15749125], [0.60816707, 3.30868089, 7.02751862]]
]

point_neighbors = find_point_neighbors(triangles)

# Example: Print neighbors of a specific point
specific_point = (8.86269454, 6.12422312, 5.03115589)
if specific_point in point_neighbors:
    print(f"Neighbors of {specific_point}:")
    for neighbor in point_neighbors[specific_point]:
        print(neighbor)
else:
    print(f"{specific_point} is not in the list of points.")
