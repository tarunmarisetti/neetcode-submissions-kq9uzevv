class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stk=[]
        for i ,temp in enumerate(temperatures):
            while stk and temp>temperatures[stk[-1]]:
                res[stk[-1]]=i-stk[-1]
                stk.pop()
            stk.append(i)
        return res
            

        