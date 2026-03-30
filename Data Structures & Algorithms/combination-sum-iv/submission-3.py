class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo={}
        def dfs(remaining):
            if remaining==0:
                return 1
            if remaining in memo:
                return memo[remaining]
            
            ways=0

            for num in nums:
                if num>remaining:
                    break
                ways+=dfs(remaining-num)
            memo[remaining]=ways

            return ways
        return dfs(target)