class Solution:
    def simplifyPath(self, path: str) -> str:
        # here we should care about the '..' and the file names
        paths=path.split('/')
        # print(paths)
        stk=[]
        for char in paths:
            if char=='..':
                if stk:
                    stk.pop()
            elif char!='' and char!='.':
                stk.append(char)
        return "/"+"/".join(stk)

        