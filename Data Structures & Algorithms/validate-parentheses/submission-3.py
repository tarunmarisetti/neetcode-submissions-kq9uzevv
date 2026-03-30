class Solution:
    def isValid(self, s: str) -> bool:
        pair={']':'[','}':'{',')':'('}
        stk=[]
        for sym in s:
            if sym in pair and  stk and stk[-1]==pair[sym]:
                stk.pop()
            else:
                stk.append(sym)
        return len(stk)==0
        