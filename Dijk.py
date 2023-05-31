import sys

def dijkstra(graph, start):
    # Initialize distances with infinity for all vertices except the start vertex
    
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')

    distances[start] = 0

    # Initialize an empty set to store visited vertices
    visited = set()

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

        # Update the distances of the neighboring vertices
        for neighbor, weight in graph[min_vertex].items():
            if distances[min_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_vertex] + weight

    return distances

# Example usage
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}
#start_vertex = 'A'
start_vertex = input("Enter the start vertex: ")
shortest_distances = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)


