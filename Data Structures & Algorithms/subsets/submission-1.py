class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)
        def backtrack(index):
            res.append(path[:])
            for i in range(index,n):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)    
        return res
        