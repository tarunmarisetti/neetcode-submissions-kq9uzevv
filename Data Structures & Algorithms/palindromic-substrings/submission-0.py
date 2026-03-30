class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        s_len=len(s)
        # odd length
        for i in range(s_len):
            l=r=i
            while l>=0 and r<=s_len-1 and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        # even length
        for i in range(s_len):
            l,r=i,i+1
            while l>=0 and r<=s_len-1 and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        return count
            
        