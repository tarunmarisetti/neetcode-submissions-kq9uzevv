class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        len1=len(word1)
        len2=len(word2)
        min_len=min(len1, len2)
        i=0
        while i<min_len:
            res.append(word1[i])
            res.append(word2[i])
            i+=1

        res.append(word1[i:])
        res.append(word2[i:])
        return "".join(res)
        
        
        