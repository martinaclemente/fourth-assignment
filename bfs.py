import numpy as np
import warnings
from collections import deque

warnings.filterwarnings('ignore')

def single_source_shortest_distances(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())
    adjacency_list = {i: [] for i in range(1, n + 1)}
    
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        adjacency_list[u].append(v)
    
    distances = [-1] * (n + 1)
    distances[1] = 0  
    queue = deque([1])  
    while queue:
        current = queue.popleft()
        for neighbor in adjacency_list[current]:
            if distances[neighbor] == -1: 
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances[1:]

file_path = "rosalind_bfs.txt" 
result = single_source_shortest_distances(file_path)
print(" ".join(map(str, result)))