"""
@description: BFS algortithm implementation
@authors: Aracelli Melissa Boza Zabarburú A01662934, Adolfo Hernández Fernández A01664412, Luis Enrique Salazar Pérez A00833460
@date: 2024/07/10 
"""

from collections import deque

def read_graph(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        
        # Split the edges correctly
        edges = content.split('),(')
        edges = [edge.strip("()") for edge in edges]
        
        # Convert each edge into a tuple of integers
        edges = [tuple(map(int, edge.split(','))) for edge in edges if edge]
    
    # Create an adjacency list representation of the graph
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

# BFS Algorithm
def bfs(graph):
    
    # Step 2: BFS initialization
    root = 1
    queue = deque([root])  # Queue for BFS
    visited = set([root])  # Set of visited nodes
    L = []  # Ordered list of visited nodes
    
    # Step 3: BFS Process
    iteration = 0
    while queue:
        # Display current state of the graph traversal
        print(f"Iteration {iteration}")
        print(f"Traversed Graph: {list(L)}")
        print(f"Queue: {list(queue)}")
        print(f"Visited: {list(visited)}")
        print("-" * 30)
        
        iteration += 1
        current = queue.popleft()
        L.append(current)  # Append to BFS order
        
        # Explore the neighbors
        for neighbor in sorted(graph[current]):  # Sort to maintain order
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # Final ordered list of visited nodes
    
    print(f'BFS Traversal Order: {L}')
    return L

# Step 1: Build the graph
graph = read_graph("bfs.txt")

bfs(graph)

