class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dfs(i,nums, cache):
            if i>=len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            rob=nums[i]+dfs(i+2, nums, cache)
            skip=dfs(i+1, nums, cache)

            cache[i]=max(rob, skip)
            return cache[i]
        
        rob1=dfs(0, nums[:-1], {})
        rob2=dfs(0, nums[1:],{})
        return max(rob1, rob2)
