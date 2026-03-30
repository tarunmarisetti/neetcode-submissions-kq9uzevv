class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        cache={}
        def dfs(i):
            if i==len(s):
                return 0
            if i in cache:
                return cache[i]
            res=1+dfs(i+1)  # skip the curr char , if we are skipping then we should add 1
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    res=min(res, dfs(j+1)) # the problem is to minimize the missing chars
                    # so we should get the min from res and the remaining substring
                
            cache[i]=res
            return res
        return dfs(0)
