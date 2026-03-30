class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        
        q=deque([(beginWord, 1)])

        while q:
            currWord,steps=q.popleft()
            if currWord==endWord:
                return steps
            
            # generate the words
            for i in range(len(currWord)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord=currWord[:i]+char+currWord[i+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        q.append((newWord, steps+1))
        return 0

            


        