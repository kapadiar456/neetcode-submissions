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
                res = dfs(pre)
                if res == False:
                    return False
            visited.remove(course)
            return True
        for i in range(numCourses):
            val = dfs(i)
            if val == False:
                return False
        return True




