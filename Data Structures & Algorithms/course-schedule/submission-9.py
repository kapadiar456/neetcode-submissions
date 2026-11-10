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
            visited.remove(course)
            hashmap[course] = []
            return True
        for i in range(numCourses):
            res = dfs(i)
            if res == False:
                return False
        return True





