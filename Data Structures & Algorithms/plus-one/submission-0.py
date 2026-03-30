class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        carry=1
        for i in range(len(digits)-1,-1,-1):
            new_digit=carry+digits[i]
            carry,mod=divmod(new_digit,10)
            res.append(mod)
        if carry!=0:
            res.append(carry) 
        return res[::-1]


        