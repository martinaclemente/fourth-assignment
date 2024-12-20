import numpy as np
import warnings

warnings.filterwarnings('ignore')

def count_connected_components(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())
    
    adjacency_list = {i: [] for i in range(1, n + 1)}
    
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    def dfs(node, visited):
        visited[node] = True
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited)
    
    visited = {i: False for i in range(1, n + 1)}
    connected_components = 0
    
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            connected_components += 1
            dfs(vertex, visited)
    
    return connected_components

file_path = "rosalind_cc.txt"  
result = count_connected_components(file_path)
print(result)