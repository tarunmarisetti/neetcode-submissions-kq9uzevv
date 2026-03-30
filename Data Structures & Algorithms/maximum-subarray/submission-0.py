class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            if currSum+nums[i]>nums[i]:
                currSum=currSum+nums[i]
            else:
                currSum=nums[i]
            if currSum>maxSum:
                maxSum=currSum
        return maxSum
        