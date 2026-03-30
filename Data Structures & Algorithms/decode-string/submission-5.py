class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        for char in s:
            if char==']':
                subString=""
                while stk and stk[-1]!='[':
                    subString=stk.pop()+subString
                stk.pop()
                count=""
                while stk and stk[-1].isdigit():
                    count=stk.pop()+count
                stk.append(int(count)*subString)
            else:
                stk.append(char)
        return ''.join(stk)
            

        