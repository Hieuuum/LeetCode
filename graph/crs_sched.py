class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, req in prerequisites:
            preMap[course].append(req)
        
        visitSet = set()
        
        def dfs(course):
            if not preMap[course]:
                return True
            elif course in visitSet:
                return False
            
            visitSet.add(course)
            for req in preMap[course]:
                if not dfs(req):
                    return False
            # visitSet.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 
            