import math

def bellman_ford(n, edges):
    dist = [math.inf] * (n + 1)
    dist[0] = 0  

    for _ in range(n - 1):  
        for u, v, weight in edges:
            if dist[u] != math.inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in edges:
        if dist[u] != math.inf and dist[u] + weight < dist[v]:
            return 1  
    return -1  


def solve(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    k = int(lines[0].strip())
    idx = 1
    results = []

    for graph_idx in range(k):
        try:
            print(f"Processing graph {graph_idx + 1}...")
            while idx < len(lines) and not lines[idx].strip():
                idx += 1  

            n, m = map(int, lines[idx].strip().split())
            idx += 1
            edges = []

            for _ in range(m):
                while idx < len(lines) and not lines[idx].strip():
                    idx += 1 
                
                if idx < len(lines):
                    u, v, weight = map(int, lines[idx].strip().split())
                    edges.append((u, v, weight))
                    idx += 1

            for i in range(1, n + 1):
                edges.append((0, i, 0)) 
            
            result = bellman_ford(n, edges)
            results.append(str(result))
        except Exception as e:
            print(f"Error processing graph {graph_idx + 1}: {e}")
            results.append("-1")

    return ' '.join(results)

file_path = "rosalind_nwc.txt" 
result = solve(file_path)
print(result)