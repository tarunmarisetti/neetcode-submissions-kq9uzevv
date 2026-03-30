class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        prev_interval=intervals[0]
        res=[]
        for curr_interval in intervals[1:]:
            if curr_interval[0]<=prev_interval[1]:
                prev_interval[1]=max(prev_interval[1],curr_interval[1])
            else:
                res.append(prev_interval)
                prev_interval=curr_interval
        res.append(prev_interval)
        return res
        