class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        cache={}
        def dfs(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if i in cache:
                return cache[i]

            # considering single digit
            single= dfs(i+1)
            double=0
            # considering double digit
            if i+1<n and '10'<=s[i:i+2]<='26':
                double= dfs(i+2)
            cache[i]= single+double
            return cache[i]
        return dfs(0)
        