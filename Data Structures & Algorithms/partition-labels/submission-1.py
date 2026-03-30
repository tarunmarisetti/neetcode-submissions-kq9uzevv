class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map={}
        for i,char in enumerate(s):
            if char not in last_index_map:
                last_index_map[char]=0
            last_index_map[char]=i
        
        res=[]
        size=0
        last_indx=0
        for i, char in enumerate(s):
            size+=1
            last_indx=max(last_indx, last_index_map[char])
            if last_indx==i:
                res.append(size)
                size=0
        return res

        