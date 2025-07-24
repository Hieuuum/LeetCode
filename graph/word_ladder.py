# 127. Word Ladder (Hard)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neigh[pattern].append(word)
        
        q = deque([beginWord])
        visitedSet = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in neigh[pattern]:
                        if neiWord not in visitedSet:
                            visitedSet.add(neiWord)
                            q.append(neiWord)
            res += 1
    
        return 0