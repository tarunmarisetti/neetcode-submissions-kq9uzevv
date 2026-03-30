class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in memo:
                return memo[i]

            count=0
            count+=dfs(i+1)

            if i+1<len(s) and '10'<=s[i:i+2]<='26':
                count+=dfs(i+2)
            memo[i]=count
            return memo[i]
        return dfs(0)
        

        