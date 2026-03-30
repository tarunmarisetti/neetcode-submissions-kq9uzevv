class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        queue=deque([(beginWord,1)])
        while queue:
            word,count=queue.popleft()
            if word==endWord:
                return count
            for char in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(word)):
                    if char==word[i]:
                        continue
                    new_word=word[:i]+char+word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word,count+1))
                        wordList.remove(new_word)
        return 0