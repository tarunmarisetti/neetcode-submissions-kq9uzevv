class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map={}
        for i, char in enumerate(s):
            last_index_map[char]=i
        res=[]
        size=0
        char_last_indx=0
        for i, char in enumerate(s):
            size+=1
            char_last_indx=max(char_last_indx, last_index_map[char])
            if char_last_indx==i:
                res.append(size)
                size=0
        return res


        