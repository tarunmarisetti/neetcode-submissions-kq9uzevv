class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can solve this probelm by considering the every char as a middle and expanding towars left and right
        res=''
        resLen=0
        s_len=len(s)
        # oddlength
        for i in range(s_len):
            l=r=i
            while l>=0 and r<=s_len-1 and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        # evenlength
        for i in range(s_len):
            l,r=i,i+1
            while l>=0 and r<=s_len-1 and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
        

        