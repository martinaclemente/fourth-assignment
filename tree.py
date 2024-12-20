import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def read_input(file_name):
    if file_name.endswith(".txt"):
        with open(file_name, 'r') as file:
            lines = file.readlines()
    
        n = int(lines[0].strip())

        edges = [list(map(int, line.strip().split())) for line in lines[1:]]
        edges_df = pd.DataFrame(edges, columns=["node1", "node2"])
    
    elif file_name.endswith(".fasta"):
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file if not line.startswith(">")]
        n = int(lines[0])
        
      
        edges = [list(map(int, line.split())) for line in lines[1:]]
        edges_df = pd.DataFrame(edges, columns=["node1", "node2"])
    
    return n, edges_df

def find_connected_components(n, edges_df):
    adj_matrix = np.zeros((n, n), dtype=int)
	
    for _, edge in edges_df.iterrows():
        node1, node2 = edge["node1"], edge["node2"]
        adj_matrix[node1 - 1, node2 - 1] = 1
        adj_matrix[node2 - 1, node1 - 1] = 1 
    
    visited = np.zeros(n, dtype=bool)
    num_components = 0
    
    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in range(n):
                if adj_matrix[current, neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    for node in range(n):
        if not visited[node]:
            num_components += 1
            visited[node] = True
            dfs(node)
    
    return num_components

def minimum_edges_to_add(n, edges_df):
    num_components = find_connected_components(n, edges_df)
    return num_components - 1

def main(file_name):
    n, edges_df = read_input(file_name)
    result = minimum_edges_to_add(n, edges_df)
    print(result)

file_name = "rosalind_tree.txt" 
if __name__ == "__main__":
    main(file_name)