class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=deque([(beginWord, 1)])
        alphabets='abcdefghijklmnopqrstuvwxyz'
        while q:
            word, count=q.popleft()
            if word==endWord:
                return count
            for char in alphabets:
                for i in range(len(word)):
                    newWord=word[:i]+char+word[i+1:]
                    if newWord in wordList:
                        q.append((newWord, count+1))
                        wordList.remove(newWord)
        return 0



        
        
        