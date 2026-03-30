class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        its the same question as LPS
        in longest Palindromic substring we return the max LPS
        here we need the count of every parlindrome'''

        count=0
        n=len(s)
        # even length
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        
        # odd length
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        return count
        
        