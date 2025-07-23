# 323. Number of Connected Components in an Undirected Graph (Medium)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = [False] * n

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            for neigh in adj[node]:
                if not visit[neigh]:
                    visit[neigh] = True
                    dfs(neigh)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        
        return res