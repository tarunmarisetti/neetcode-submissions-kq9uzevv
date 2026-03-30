class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]

        for char in s:
            if char==']':
                encoded_string=''
                while stk and stk[-1]!='[':
                    encoded_string=stk.pop()+encoded_string
                stk.pop()
                k=''
                while stk and stk[-1].isdigit():
                    k=stk.pop()+k
                stk.append(int(k)*encoded_string)
            else:
                stk.append(char)
        return "".join(stk)
                
        