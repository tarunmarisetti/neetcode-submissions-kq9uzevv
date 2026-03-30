class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        path=[]
        def backtrack(start, total):
            if total==target and path not in res:
                res.append(path[:])
            if total>target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i+1, total+candidates[i])
                path.pop()
        backtrack(0,0)
        return res
        