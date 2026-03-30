class Solution:
    def isValid(self, s: str) -> bool:
        pair={']':'[','}':'{',')':'('}
        stk=[]
        for sym in s:
            if sym in pair:
                if stk and stk[-1]==pair[sym]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(sym)
        return len(stk)==0
        