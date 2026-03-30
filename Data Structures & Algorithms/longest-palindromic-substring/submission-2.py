class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        res_len=0
        n=len(s)

        # even len
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                curr_len=r-l+1
                if curr_len>res_len:
                    res=s[l:r+1]
                    res_len=curr_len
                l-=1
                r+=1
            
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                curr_len=r-l+1
                if curr_len>res_len:
                    res=s[l:r+1]
                    res_len=curr_len
                l-=1
                r+=1
                
        return res
        
        

        