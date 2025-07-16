# 212. Word Search II (Hard)

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, cur):
            if (r < 0 or c < 0 or r >= len(board) 
                or c >= len(board[0]) or (r, c) in marked
                or board[r][c] not in cur.children):
                return 

            marked.add((r, c))
            cur = cur.children[board[r][c]]
            if cur.word:
                res.append(cur.word)
                cur.word = None

            dfs(r+1, c, cur)
            dfs(r, c+1, cur)
            dfs(r, c-1, cur)
            dfs(r-1, c, cur)
            marked.remove((r, c))

        
        def addWord(i, word, cur):
            if i >= len(word):
                cur.word = word
                return
            elif word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            return addWord(i+1, word, cur.children[word[i]])
            
        self.root = TrieNode()
        cur = self.root
        res, marked = [], set()

        for word in words:
            addWord(0, word, cur)

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, cur)

        return res