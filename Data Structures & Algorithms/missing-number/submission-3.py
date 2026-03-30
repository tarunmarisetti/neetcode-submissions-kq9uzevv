class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_sum=0
        for i in range(len(nums)+1):
            num_sum+=i
        return num_sum-sum(nums)

        