class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        path=[]
        is_used=[False]*n
        def backtrack():
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(n):
                if not is_used[i]:
                    path.append(nums[i])
                    is_used[i]=True
                    backtrack()
                    path.pop()
                    is_used[i]=False
        backtrack()
        return res
            
        