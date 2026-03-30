class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        word1_len=len(word1)
        word2_len=len(word2)
        res=''
        while i<word1_len and j<word2_len:
            res+=word1[i]+word2[j]
            i+=1
            j+=1
        while i<word1_len:
            res+=word1[i]
            i+=1
        while j<word2_len:
            res+=word2[j]
            j+=1
        return res
        
        