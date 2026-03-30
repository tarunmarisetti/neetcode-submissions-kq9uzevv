class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)
        counter=Counter(nums)
        def backtrack():
            if len(path)==n:
                res.append(path[:])
                return
            for num in counter:
                if counter[num]>0:
                    path.append(num)
                    counter[num]-=1
                    backtrack()
                    counter[num]+=1
                    path.pop()
        backtrack()
        return res

        