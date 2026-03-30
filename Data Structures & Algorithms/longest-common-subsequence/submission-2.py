class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len,text2_len=len(text1),len(text2)
        dp=[[0]*(text2_len+1) for _ in range(text1_len+1)]
        for i in range(text1_len-1,-1,-1):
            for j in range(text2_len-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        