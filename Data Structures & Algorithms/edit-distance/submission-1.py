class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.count=0
        def dfs(i,j):
            # insert all remaining characters of word2.
            if i==len(word1):
                return len(word2)-j
            # delete all remaining characters of word1.
            if j==len(word2):
                return len(word1)-i
            
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            else:
               return 1+min(dfs(i,j+1),dfs(i+1,j),dfs(i+1, j+1))
        return dfs(0,0)
        