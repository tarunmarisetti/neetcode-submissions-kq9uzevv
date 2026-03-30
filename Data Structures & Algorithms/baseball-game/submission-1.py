class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for operation in operations:
            if operation=='+':
                prev1=stk[-1]
                prev2=stk[-2]
                stk.append(prev1+prev2)
            elif operation=='D':
                prev=stk[-1]
                stk.append(2*prev)
            elif operation=='C':
                stk.pop()
            else:
                stk.append(int(operation))
        return sum(stk)
        