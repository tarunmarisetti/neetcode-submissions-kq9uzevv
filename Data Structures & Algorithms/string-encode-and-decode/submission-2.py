class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s))+'#'+s for s in strs)


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        s_len=len(s)
        while i<s_len:
            j=i
            while s[j]!='#':
                j+=1
            word_len=int(s[i:j])
            i=j+1
            res.append(s[i:i+word_len])
            i=i+word_len
        return res
