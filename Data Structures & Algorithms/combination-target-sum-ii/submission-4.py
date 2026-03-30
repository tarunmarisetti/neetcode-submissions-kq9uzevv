class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # cause of duplicates and prune the tree if the currsum is >target earlier
        res=[]
        path=[]
        def backtrack(index, currSum):
            if currSum==target:
                res.append(path[:])
                
            if currSum>target:
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i-1]==candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, currSum+candidates[i])
                path.pop()
        backtrack(0,0)
        return res
        