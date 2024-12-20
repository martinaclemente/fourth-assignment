import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def calculate_vertex_degrees(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())
    
    degrees = np.zeros(n, dtype=int)
    
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    
    return degrees

file_path = "rosalind_deg.txt"  
degrees = calculate_vertex_degrees(file_path)
print(" ".join(map(str, degrees)))