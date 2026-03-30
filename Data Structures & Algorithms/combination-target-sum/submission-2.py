class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        path=[]
        def backtrack(i, currSum):
            if currSum==target:
                res.append(path[:])
            if currSum>target:
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(j, currSum+nums[j])
                path.pop()
        backtrack(0,0)
        return res
        