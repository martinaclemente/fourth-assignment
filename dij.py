import numpy as np
import warnings
from heapq import heappop, heappush  

warnings.filterwarnings('ignore')

def dijkstra_shortest_path(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())
    
    adjacency_list = {i: [] for i in range(1, n + 1)}
    
    for line in lines[1:]:
        u, v, w = map(int, line.strip().split())
        adjacency_list[u].append((v, w))
    
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[1] = 0
    visited = set()
    priority_queue = [(0, 1)]
    
    while priority_queue:
        current_distance, current_vertex = heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        
        for neighbor, weight in adjacency_list[current_vertex]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heappush(priority_queue, (new_distance, neighbor))
    
    result = [distances[i] if distances[i] != float('inf') else -1 for i in range(1, n + 1)]
    return result

file_path = "rosalind_dij.txt"  
result = dijkstra_shortest_path(file_path)
print(" ".join(map(str, result)))