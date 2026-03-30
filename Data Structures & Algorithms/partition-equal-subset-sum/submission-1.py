class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        memo={}

        def dfs(i,remaining_sum):
            if (i,remaining_sum) in memo:
                return memo[(i,remaining_sum)]
            if remaining_sum==0:
                return True
            if i>=len(nums) or remaining_sum<0:
                return False
            take=dfs(i+1,remaining_sum-nums[i])
            skip=dfs(i+1, remaining_sum)
            memo[(i,remaining_sum)]=take or skip
            return memo[(i,remaining_sum)]
        return dfs(0,target)
        