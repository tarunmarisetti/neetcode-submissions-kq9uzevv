class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr=0
        n=len(nums)
        for i in range(n):
            xorr^=i ^ nums[i]
        return xorr^n