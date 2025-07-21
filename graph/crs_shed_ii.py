# 210. Course Schedule II (Medium)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: set() for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, req in prerequisites:
            adj[req].add(course)
            in_degree[course] += 1
        
        queue, res = [], []
        for c in range(numCourses):
            if in_degree[c] == 0:
                queue.append(c)
                res.append(c)
        queue = collections.deque(queue)

        takenCourses = 0
        while queue:
            prereq = queue.popleft()
            takenCourses += 1
            for c in adj[prereq]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
                    res.append(c)
        
        return res if takenCourses == numCourses else []