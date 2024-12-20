import heapq
import math

def dijkstra(n, graph, start):
    dist = [math.inf] * (n + 1)
    dist[start] = 0
    pq = [(0, start)] 

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def find_shortest_cycle(n, graph, edge):
    u, v, weight = edge
    
    modified_graph = {i: [] for i in range(1, n + 1)}
    for node in graph:
        modified_graph[node] = graph[node][:]  
    modified_graph[u] = [edge for edge in modified_graph[u] if edge[0] != v]  
    
    dist_from_v = dijkstra(n, modified_graph, v)
    
    if dist_from_v[u] == math.inf:
        return -1  
    
    cycle_length = dist_from_v[u] + weight
    return cycle_length

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
            graph = {i: [] for i in range(1, n + 1)}

            edges = []
            for _ in range(m):
                while idx < len(lines) and not lines[idx].strip():
                    idx += 1  
                
                if idx < len(lines):
                    u, v, weight = map(int, lines[idx].strip().split())
                    graph[u].append((v, weight))
                    edges.append((u, v, weight))
                    idx += 1
            
            first_edge = edges[0]

            cycle_length = find_shortest_cycle(n, graph, first_edge)
            results.append(str(cycle_length))
        except Exception as e:
            print(f"Error processing graph {graph_idx + 1}: {e}")
            results.append("-1")

    return ' '.join(results)

file_path = "rosalind_cte.txt" 
result = solve(file_path)
print(result)