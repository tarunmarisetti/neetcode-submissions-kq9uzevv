class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len=len(s1)
        s2Len=len(s2)
        s3Len=len(s3)
        if s1Len+s2Len!=s3Len:
            return False
        
        memo={}
        def dfs(i,j):
            if i==s1Len and j==s2Len:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            k=i+j
            ans=False
            if i<s1Len and s1[i]==s3[k]:
                ans=dfs(i+1,j)
            if not ans and j<s2Len and s2[j]==s3[k]:
                ans=dfs(i, j+1)
            memo[(i,j)]=ans
            return ans
        return dfs(0,0)



        