class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''to get longest substring palindrom 2 possibel cases
        1. the LPS is odd
        2. the LPS is even'''
        # use 2 pointers for substring

        # finding even len
        res=""
        resLen=float('-inf')
        n=len(s)
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if resLen<(r-l+1):
                    resLen=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                if resLen<(r-l+1):
                    resLen=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        return res


        