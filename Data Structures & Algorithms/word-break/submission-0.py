class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                word_len=len(word)
                if i+word_len<=n and s[i:i+word_len]==word:
                    dp[i]=dp[i+word_len]
                if dp[i]:
                    break
        return dp[0]
        