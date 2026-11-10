class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

            

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph:
            if dst in self.graph[src]:
                self.graph[src].remove(dst)
                return True
            else:
                return False
        else:
            return False

    def dfs(self, node, destination, visit):
        if node in visit:
            return 0
        if node == destination:
            return 1
        count=0
        visit.add(node)
        for adj in self.graph[node]:
            count+= self.dfs(adj, destination, visit)
        visit.remove(node)
        return count

    def hasPath(self, src: int, dst: int) -> bool:
        if self.dfs(src, dst, set())>=1:
            return True
        else:
            return False
