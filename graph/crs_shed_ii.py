# 210. Course Schedule II (Medium)

# Kahn's Algorithm
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
    
# 3-State DFS

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         adj = {c:[] for c in range(numCourses)}
#         # 0: univisited, 1: visiting, 2:visited
#         visitState = [0] * numCourses
#         res = []

#         for course, req in prerequisites:
#             adj[course].append(req)
        
#         def hasCycle(c):
#             if visitState[c] == 2:
#                 return False
#             elif visitState[c] == 1:
#                 return True
            
#             visitState[c] = 1

#             for req in adj[c]:
#                 if hasCycle(req):
#                     return True
            
#             visitState[c] = 2
#             res.append(c)
#             return False
        
#         for c in range(numCourses):
#             if visitState[c] == 0:
#                 if hasCycle(c):
#                     return []
        
#         return res