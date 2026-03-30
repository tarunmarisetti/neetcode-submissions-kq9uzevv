class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def backtrack(i,path):
            res.append(path[:])
            for j in range(i,n):
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        return res
        