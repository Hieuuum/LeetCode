# 261. Graph Valid Tree (Medium)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        q = deque([0])
        visited.add(0)

        while q:
            node = q.popleft()
            for neigh in adj[node]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        
        return len(visited) == n