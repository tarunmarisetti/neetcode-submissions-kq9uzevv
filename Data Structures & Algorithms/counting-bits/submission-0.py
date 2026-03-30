class Solution:
    def getNoOfOnes(self,num):
        res=0
        while num:
            if num & 1:
                res+=1
            num=num>>1
        return res


    def countBits(self, n: int) -> List[int]:
        res=[0]
        for i in range(1,n+1):
            res.append(self.getNoOfOnes(i))
        return res

       
        