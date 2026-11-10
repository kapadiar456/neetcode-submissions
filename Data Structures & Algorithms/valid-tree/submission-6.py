class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(n)}
        for e1, e2 in edges:
            hashmap[e1].append(e2)
            hashmap[e2].append(e1)
        visited = set()
        def dfs(edge, parent):
            if edge in visited:
                return False
            visited.add(edge)
            for neigh in hashmap[edge]:
                if neigh == parent:
                    continue
                res = dfs(neigh, edge)
                if res == False:
                    return False
            return True
        res = dfs(0, 0)
        if len(visited) == n and res == True:
            return True
        else:
            return False