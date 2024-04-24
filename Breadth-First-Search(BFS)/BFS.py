# Breadth-First Search explores all neighbor nodes at the present depth before moving on to nodes at the next level of depth.
# It uses a queue for traversal.
graph = {
    'Arad': {'Zerind', 'Sibiu', 'Timisoara'},
    'Zerind': {'Oradea', 'Arad'},
    'Oradea': {'Zerind', 'Sibiu'},
    'Sibiu': {'Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'},
    'Timisoara': {'Arad', 'Lugoj'},
    'Lugoj': {'Timisoara', 'Mehadia'},
    'Mehadia': {'Lugoj', 'Drobeta'},
    'Drobeta': {'Mehadia', 'Craiova'},
    'Craiova': {'Drobeta', 'Rimnicu Vilcea', 'Pitesti'},
    'Rimnicu Vilcea': {'Sibiu', 'Craiova', 'Pitesti'},
    'Fagaras': {'Sibiu', 'Bucharest'},
    'Pitesti': {'Rimnicu Vilcea', 'Craiova', 'Bucharest'},
    'Bucharest': {'Fagaras', 'Pitesti'}
}
from queue import Queue

def bfs_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    came_from = {}
    visited[start] = True
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                came_from[neighbor] = current
                frontier.put(neighbor)
    
    return None

# Example usage
start = 'Arad'
goal = 'Bucharest'
path = bfs_search(graph, start, goal)
if path:
    print("Shortest path from", start, "to", goal, ":", path)
else:
    print("No path found from", start, "to", goal)
