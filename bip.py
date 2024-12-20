from collections import deque

def is_bipartite(graph, n):
    colors = [-1] * (n + 1)

    for node in range(1, n + 1):
        if colors[node] == -1: 
            queue = deque([node])
            colors[node] = 0 

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if colors[v] == -1: 
                        colors[v] = 1 - colors[u]  
                        queue.append(v)
                    elif colors[v] == colors[u]:  
                        return False  
    return True 

def check_bipartite(file_path):
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

            if idx < len(lines):
                n, m = map(int, lines[idx].strip().split())
                idx += 1
            else:
                results.append("Error")
                continue
            
            graph = {i: [] for i in range(1, n + 1)}

            for _ in range(m):
                while idx < len(lines) and not lines[idx].strip():  
                    idx += 1
                
                if idx < len(lines):
                    u, v = map(int, lines[idx].strip().split())
                    graph[u].append(v)
                    graph[v].append(u) 
                    idx += 1
                else:
                    results.append("Error")
                    break

            if is_bipartite(graph, n):
                results.append("1")
            else:
                results.append("-1")
        except Exception as e:
            print(f"Error processing graph {graph_idx + 1}: {e}")
            results.append("Error")

    return ' '.join(results)

file_path = "rosalind_bip.txt"
result = check_bipartite(file_path)
print(result)