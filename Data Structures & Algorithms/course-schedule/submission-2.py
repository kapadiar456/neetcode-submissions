class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        myMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            myMap[crs].append(pre)

        def dfs(crs, visited):
            if myMap[crs] == None:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for course in myMap[crs]:
                if dfs(course, visited) == False:
                    return False
            return True

        for course in range(numCourses):
            visited = set()
            if dfs(course, visited) == False:
                return False
        return True
