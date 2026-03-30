class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(', '}':'{', ']':'['}
        stk=[]
        for sign in s:
            if sign in pairs:
                if stk and stk[-1]==pairs[sign]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(sign)
        return len(stk)==0

        