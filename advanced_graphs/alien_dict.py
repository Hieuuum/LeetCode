# 269. Alien Dictionary (Hard)

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for c in range(len(w1)):
                if w1[c] != w2[c]:
                    adj[w1[c]].add(w2[c])
                    break
        
        visit = {} #false: visited, true: visited & in path
        path = []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            path.append(c)
            visit[c] = False
        
        for c in adj:
            if dfs(c):
                return ""
        
        path.reverse()
        return "".join(path)
        
