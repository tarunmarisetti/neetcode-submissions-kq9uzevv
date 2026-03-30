class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # as we iterate trough the nums we will keep track of both max of positive and negative
        currMax=currMin=1
        res=nums[0]
        for n in nums:
            temp=currMax*n
            currMax=max(currMax*n, currMin*n, n)
            currMin=min(temp,currMin*n,n)
            res=max(res,currMax)
        return res

        