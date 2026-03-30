class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n+1)]
        dp[0][0]=1 # there is count of 1 to make sum 0 with zero nums
        for i in range(n):
            for curr_sum,count in dp[i].items():
                dp[i+1][curr_sum+nums[i]]+=count
                dp[i+1][curr_sum-nums[i]]+=count
        return dp[n][target]

        