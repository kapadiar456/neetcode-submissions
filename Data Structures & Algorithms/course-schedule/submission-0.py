class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for req in premap[crs]:
                valid = dfs(req)
                if valid == False:
                    return False
            visitSet.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True