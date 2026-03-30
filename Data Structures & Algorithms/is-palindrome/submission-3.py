class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_set='abcdefghijklmnopqrstuvwxyz0123456789'
        l,r=0,len(s)-1
        while l<r:
            while l<r and s[l].lower() not in char_set:
                l+=1
            while l<r and s[r].lower() not in char_set:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        