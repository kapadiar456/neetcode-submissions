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
        for i in range(n):
            if i not in visited:
                dfs(i, i)
                count+=1
        return count