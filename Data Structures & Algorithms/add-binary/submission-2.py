class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen=len(a)
        bLen=len(b)
        i,j=aLen-1,bLen-1
        carry=0
        res=[]
        while carry or i>=0 or j>=0:
           
            aDigit=int(a[i]) if i>=0 else 0
            bDigit=int(b[j]) if j>=0 else 0
            total=aDigit+bDigit+carry

            currNum=total%2
            carry=total//2
            res.append(str(currNum))
            i-=1
            j-=1
        return "".join(reversed(res))


        