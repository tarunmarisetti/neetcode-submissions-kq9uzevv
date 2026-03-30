class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stk=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]]<temp:
                currIndex=stk.pop()
                res[currIndex]=i-currIndex
            stk.append(i)
        return res
        