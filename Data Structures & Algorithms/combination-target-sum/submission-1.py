class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        res=[]
        path=[]
        n=len(nums)
        def backtrack(index,currSum):
            if currSum==target:
                res.append(path[:])
                return
            if currSum>target:
                return
            for i in range(index,n):
                path.append(nums[i])
                backtrack(i,currSum+nums[i])
                path.pop()
        backtrack(0,0)
        return res
        