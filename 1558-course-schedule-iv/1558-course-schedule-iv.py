class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        f = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            f[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if f[i][k] and f[k][j]:
                        f[i][j] = True
        return [f[a][b] for a, b in queries]