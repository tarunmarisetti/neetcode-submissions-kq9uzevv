class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
       # For circular subarray, the maximum sum can occur in two ways:
        # 1) Normal subarray (non-circular) → classic Kadane using currMax / globMax
        # 2) Circular subarray (wrap-around)
        #
        # A circular max subarray means we take elements from the end and beginning.
        # This is equivalent to removing a contiguous subarray in the middle
        # that has the MINIMUM sum.
        #
        # So:
        #   circularMax = totalSum - minimumSubarraySum
        #
        # To compute minimum subarray sum efficiently, we run a "reverse Kadane":
        #   - currMin tracks the minimum sum subarray ending at current index
        #   - globMin tracks the overall minimum subarray sum seen so far
        #
        # We take:
        #   max(globMax, totalSum - globMin)
        #
        # Edge case:
        # If all numbers are negative, globMax is the answer
        # (totalSum - globMin would incorrectly give 0, which is invalid)

        globalMax=globalMin=nums[0]
        currMin=currMax=0
        total=0
        for num in nums:
            total+=num
            currMin=min(num, num+currMin)
            currMax=max(num, num+currMax)
            globalMin=min(globalMin, currMin)
            globalMax=max(globalMax, currMax)
        return max(globalMax, total-globalMin) if globalMax>0 else globalMax

