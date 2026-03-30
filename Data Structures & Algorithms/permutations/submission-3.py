class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        isUsed=[False]*n
        res=[]
        def backtrack(path):
            if len(path)==n:
                res.append(path[:])
            
            for i in range(n):
                if not isUsed[i]:
                    isUsed[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    isUsed[i]=False
        backtrack([])
        return res


        