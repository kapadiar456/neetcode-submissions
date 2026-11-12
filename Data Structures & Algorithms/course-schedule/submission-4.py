class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            hashmap[c1].append(c2)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                return True
            visited.add(course)
            for pre in hashmap[course]:
                if dfs(pre) == False:
                    return False
                else:
                    return True
        return dfs(0)




