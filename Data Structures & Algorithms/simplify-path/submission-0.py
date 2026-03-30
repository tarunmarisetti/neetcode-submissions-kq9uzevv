class Solution:
    def simplifyPath(self, path: str) -> str:
        stk=[]
        paths=path.split("/")
        # print(paths)
        for curr in paths:
            if curr=="..":
                if stk:
                    stk.pop()
            elif curr!="" and curr!=".":
                stk.append(curr)
        return "/" + "/".join(stk)
        