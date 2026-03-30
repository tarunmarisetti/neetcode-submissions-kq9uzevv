class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i], 1+LIS[j])
        print(LIS)
        return max(LIS)
        