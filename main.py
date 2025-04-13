def hamiltonian_path(graph):
    n = len(graph)
    path = []

    def backtrack(v, visited):
        path.append(v)
        if len(path) == n:
            return True
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if backtrack(u, visited):
                    return True
                visited[u] = False
        path.pop()
        return False

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path.clear()
        if backtrack(start, visited):
            return path
    return None
