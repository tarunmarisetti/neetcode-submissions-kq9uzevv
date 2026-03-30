class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculation(a,b,operator):
            if operator=='+':
                return a+b
            elif operator=='-':
                return a-b
            elif operator=='*':
                return a*b
            else:
                return int(a/b)
        
        stk=[]
        for token in tokens:
            if token in '+-*/':
                b=stk.pop()
                a=stk.pop()
                val=calculation(a,b,token)
                stk.append(val)
            else:
                stk.append(int(token))
        return stk[-1]
        