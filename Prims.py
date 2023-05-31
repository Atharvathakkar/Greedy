import sys

def prim(graph, start):
    # Initialize the minimum spanning tree and the set of visited vertices
    mst = {}
    visited = set()

    # Initialize distances with infinity for all vertices except the start vertex
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')

    distances[start] = 0

    while len(visited) != len(graph):
        # Find the vertex with the minimum distance from the start vertex
        min_distance = sys.maxsize
        min_vertex = None

        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Mark the current vertex as visited
        visited.add(min_vertex)

        # Add the current vertex and its corresponding edge to the minimum spanning tree
        if min_vertex != start:
            mst[min_vertex] = distances[min_vertex]

        # Update the distances of the neighboring vertices
        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited and weight < distances[neighbor]:
                distances[neighbor] = weight

    return mst

# Example usage
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}
start_vertex = 'A'

minimum_spanning_tree = prim(graph, start_vertex)

print("Minimum Spanning Tree:")
for vertex, weight in minimum_spanning_tree.items():
    print(start_vertex, "-", vertex, ":", weight)

