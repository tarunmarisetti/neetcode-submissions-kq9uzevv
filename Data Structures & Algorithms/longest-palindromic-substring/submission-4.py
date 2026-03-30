class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''using two pointers for substring and recursive for subsequence
        2 possible cases len of string is
        1. odd then l and r start from same
        2. even then l and right is i, i+1'''

        def checkPalindrome(l,r):
            resLen=float('-inf')
            res=''
            while l>=0 and r<n and s[l]==s[r]:
                if resLen<r-l+1:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            return res

        n=len(s)
        res=''
        for i in range(n):
            evenPalin=checkPalindrome(i,i+1)
            oddPalin=checkPalindrome(i,i)
            res=max(res, evenPalin, oddPalin, key=len) 
        return res 
        