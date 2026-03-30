class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        def backtrack(index):
            res.append(path[:])
            for i in range(index, len(nums)):
                if i>index and nums[i-1]==nums[i]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res
        