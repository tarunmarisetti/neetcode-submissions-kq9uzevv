class Solution:

    def encode(self, strs: List[str]) -> str:
        str_=''
        for i in strs:
            str_+=i+"/"
        return str_



    def decode(self, s: str) -> List[str]:
        str_=''
        list_str=[]
        for i in s:
            if i !='/':
                str_+=i
            else:
                list_str.append(str_)
                str_=''
        return list_str
