class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            count=0
            count+=dfs(i+1)

            if i+1<len(s) and '10'<=s[i:i+2]<='26':
                count+=dfs(i+2)
            memo[i]=count
            return count
        return dfs(0)       