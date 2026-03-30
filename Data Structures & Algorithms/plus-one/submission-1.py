class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q=deque()
        carry=1
        for i in range(len(digits)-1,-1,-1):
            currSum=digits[i]+carry
            rem,carry=currSum%10,currSum//10
            q.append(rem)
        if carry!=0:
            q.append(carry)
        # print(q)
        
        res=[]
        while q:
            res.append(q.pop())
        return res
