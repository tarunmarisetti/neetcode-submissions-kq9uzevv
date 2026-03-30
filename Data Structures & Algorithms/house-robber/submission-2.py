class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        n=len(nums)
        def dfs(i):
            if i>=n:
                return 0
            if i in cache:
                return cache[i]
            skip=dfs(i+1)
            rob=nums[i]+dfs(i+2)

            cache[i]= max(skip, rob)
            return cache[i]
        return dfs(0)

        