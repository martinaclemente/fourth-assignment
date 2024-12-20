import numpy as np

def read_graph(file_path):
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    n, m = map(int, lines[0].split())
    edges = []
    for line in lines[1:]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
    
    return n, edges

def topological_sort(n, edges):
    from collections import defaultdict
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((v, w))
    
    visited = np.zeros(n + 1, dtype=bool)
    topo_order = []

    def dfs(node):
        visited[node] = True
        for neighbor, _ in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        topo_order.append(node)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    return topo_order[::-1], adj_list

def shortest_path_dag(n, edges, source=1):
    topo_order, adj_list = topological_sort(n, edges)

    INF = float('inf')
    dist = np.full(n + 1, INF)
    dist[source] = 0

    for u in topo_order:
        if dist[u] != INF: 
            for v, w in adj_list[u]:
                dist[v] = min(dist[v], dist[u] + w)

    return [0 if i == source else ('x' if dist[i] == INF else int(dist[i])) for i in range(1, n + 1)]

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(" ".join(map(str, result)) + '\n')

def main():
    input_file = 'rosalind_sdag.txt'
    output_file = 'rosalind_sdag_output.txt'

    n, edges = read_graph(input_file)
    result = shortest_path_dag(n, edges, source=1)
    write_output(output_file, result)

if __name__ == "__main__":
    main()