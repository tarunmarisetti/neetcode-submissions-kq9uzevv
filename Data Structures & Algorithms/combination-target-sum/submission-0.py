class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        path=[]
        def backtrack(start,total):
            if total== target:
                res.append(path[:])
            if total>target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, total+nums[i])
                path.pop()
        backtrack(0,0)
        return res

        