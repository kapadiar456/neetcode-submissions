class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            hashmap[n1].append(n2)
            hashmap[n2].append(n1)
        def dfs(val, prev, visited):
            if val in visited:
                return
            visited.add(val)
            for nei in hashmap[val]:
                if nei == prev:
                    continue
                dfs(nei, val, visited)
            return
        
        count = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i, -1, visited)
                count+=1
        return count
            

            