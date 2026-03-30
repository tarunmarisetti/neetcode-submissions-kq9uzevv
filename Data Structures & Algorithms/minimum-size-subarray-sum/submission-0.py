class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        left=0
        prefixSum=0
        for right in range(len(nums)):
            prefixSum+=nums[right]
            while prefixSum>=target:
                min_len=min(min_len,right-left+1)
                prefixSum-=nums[left]
                left+=1
        return min_len if min_len!=float('inf') else 0
        