class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path=[]
        res=[]
        candidates.sort()
        def backtrack(index,curr_sum):
            if curr_sum==target:
                res.append(path[:])
            elif curr_sum>target:
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                curr_ele=candidates[i]
                path.append(curr_ele)
                curr_sum+=curr_ele
                backtrack(i+1,curr_sum)
                curr_sum-=curr_ele
                path.pop()
        backtrack(0,0)
        return res

        