class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
       
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(self.graph[node])
        
        print("BFS:", visited)
