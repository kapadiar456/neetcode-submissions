class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i: [] for i in range(n)}
        for e1, e2 in edges:
            hashmap[e1].append(e2)
            hashmap[e2].append(e1)
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return
            visited.add(curr)
            for neigh in hashmap[curr]:
                if neigh != prev:
                    dfs(neigh, curr)
            return
        count = 0
        for e1, e2 in edges:
            if e1 not in visited:
                dfs(e1, e1)
                count+=1
        return count