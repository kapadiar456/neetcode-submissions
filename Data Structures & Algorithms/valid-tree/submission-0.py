class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = [[] for _ in range(n)]

        for p1, p2 in edges:
            hashmap[p1].append(p2)
            hashmap[p2].append(p1)

        def dfs(val, hashmap, visited, prev):
            print(val, " ", prev)
            if val in visited and val != prev:
                return False
            visited.add(val)
            for item in hashmap[val]:
                if item == prev:
                    continue
                if dfs(item, hashmap, visited, val) == False:
                    return False
            return True
            

            
        
        visited = set()
        return dfs(0, hashmap, visited, 0)