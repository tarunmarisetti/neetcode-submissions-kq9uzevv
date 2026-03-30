class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        # here left shift the res to add the new value 
        # right shift n to get the next value
        for _ in range(32):
            res=res<<1|(n & 1)
            n=n>>1
        return res
        