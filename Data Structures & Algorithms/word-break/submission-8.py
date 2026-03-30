class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordDict=set(wordDict)
        memo={}
        def dfs(i,j):
            if i==n and j==n:
                return True
            if i<n and j==n:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i:j+1] in wordDict:
                memo[(i,j)]=(dfs(j+1,j+1) or dfs(i,j+1))
            else:
                memo[(i,j)]=dfs(i,j+1)
            return memo[(i,j)]
        return dfs(0,0)
        