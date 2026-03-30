class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        totalSum=sum(nums)
        cache={}
        def dfs(i, s1Sum):
            if i==n:
                return s1Sum==totalSum-s1Sum
            if (i,s1Sum) in cache:
                return cache[(i, s1Sum)]
            # consider
            consider=dfs(i+1, s1Sum+nums[i])
            # skip
            skip=dfs(i+1, s1Sum)
            cache[(i,s1Sum)]=consider or skip
            return cache[(i,s1Sum)]
        return dfs(0,0)
        