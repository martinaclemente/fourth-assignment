import math

def bellman_ford(n, edges, source=1):
    dist = [math.inf] * (n + 1)  
    dist[source] = 0

    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != math.inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    result = []
    for i in range(1, n + 1):
        if dist[i] == math.inf:
            result.append('x')
        else:
            result.append(str(dist[i]))
    
    return ' '.join(result)

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m = map(int, lines[0].strip().split())  
    edges = []
    
    for i in range(1, m + 1):
        u, v, weight = map(int, lines[i].strip().split())
        edges.append((u, v, weight))
    
    return n, edges

def solve(file_path):
    n, edges = parse_input(file_path)
    return bellman_ford(n, edges)

file_path = "rosalind_bf.txt" 
result = solve(file_path)
print(result)