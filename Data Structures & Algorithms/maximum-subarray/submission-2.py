class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using Kadane algo
        currSum=maxSum=float('-inf')
        for num in nums:
            if num>currSum+num:
                currSum=num
            else:
                currSum+=num
            
            if currSum>maxSum:
                maxSum=currSum
        return maxSum if maxSum!=float('-inf') else -1
        