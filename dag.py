import numpy as np
import warnings

warnings.filterwarnings('ignore')


def is_acyclic(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    k = int(lines[0].strip())
    
    results = []
    idx = 1  
    
    def has_cycle_dfs(graph, n):
        visited = [False] * (n + 1)
        rec_stack = [False] * (n + 1)

        def dfs(node):
            if rec_stack[node]:  
                return True
            if visited[node]:
                return False
            
            visited[node] = True
            rec_stack[node] = True
            
            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            
            rec_stack[node] = False
            return False
        
        for v in range(1, n + 1):
            if not visited[v]:
                if dfs(v):
                    return True
        return False
    
    for _ in range(k):
        n, m = map(int, lines[idx].strip().split())
        idx += 1
        
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            u, v = map(int, lines[idx].strip().split())
            graph[u].append(v)
            idx += 1
        
        if has_cycle_dfs(graph, n):
            results.append("-1")
        else:
            results.append("1")
    
    return results


file_path = "rosalind_dag.txt"  
result = is_acyclic(file_path)
print(" ".join(result))