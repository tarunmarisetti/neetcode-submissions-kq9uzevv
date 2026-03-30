class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        is_used=[False]* len(nums)
        n=len(nums)
        def backtrack():
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not is_used[i]:
                    is_used[i]=True
                    path.append(nums[i])
                    print(path)
                    backtrack()
                    path.pop()
                    is_used[i]=False
        backtrack()
        return res
        