class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_size=float('inf')
        prefix=0
        for right in range(len(nums)):
            prefix+=nums[right]
            while prefix>=target:
                min_size=min(min_size, (right-left+1))
                prefix-=nums[left]
                left+=1
        return min_size if min_size!=float('inf') else 0

        