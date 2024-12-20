import numpy as np
import warnings

warnings.filterwarnings('ignore')

def sum_of_neighbor_degrees(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())
    
    adjacency_list = {i: [] for i in range(1, n + 1)}
    degrees = np.zeros(n, dtype=int)
    
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    
    sum_neighbor_degrees = np.zeros(n, dtype=int)
    for vertex in range(1, n + 1):
        neighbor_degrees = [degrees[neighbor - 1] for neighbor in adjacency_list[vertex]]
        sum_neighbor_degrees[vertex - 1] = sum(neighbor_degrees)
    
    return sum_neighbor_degrees

file_path = "rosalind_ddeg.txt"  
result = sum_of_neighbor_degrees(file_path)
print(" ".join(map(str, result)))