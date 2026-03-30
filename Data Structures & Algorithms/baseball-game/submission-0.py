class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for operation in operations:
            if operation=='+':
                first=stk[-1]
                second=stk[-2]
                stk.append(first+second)
            elif operation=='D':
                prev_score=stk[-1]
                stk.append(2*prev_score)
            elif operation=='C':
                stk.pop()
            else:
                stk.append(int(operation))
        return sum(stk)
        