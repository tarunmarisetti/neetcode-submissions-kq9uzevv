class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        isUsed=[False]*n
        def backtrack(path):
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(n):
                if i>0 and nums[i] ==nums[i-1] and isUsed[i-1]:
                    continue
                if not isUsed[i]:
                    isUsed[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    isUsed[i]=False
        backtrack([])
        return res
        
        