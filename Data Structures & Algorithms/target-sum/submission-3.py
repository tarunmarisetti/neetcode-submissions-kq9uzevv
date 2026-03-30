class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=defaultdict(int)
        dp[0]=1 # there is count of 1 to make sum 0 with zero nums
        for i in range(n):
            next_dp=defaultdict(int)
            for curr_sum,count in dp.items():
                next_dp[curr_sum+nums[i]]+=count
                next_dp[curr_sum-nums[i]]+=count
            dp=next_dp
        return dp[target]

        