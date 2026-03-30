class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        prev_interval=intervals[0]
        res=[]
        for start,end in intervals[1:]:
            if start<=prev_interval[1]:
                prev_interval[1]=max(prev_interval[1],end)
            else:
                res.append(prev_interval)
                prev_interval=[start,end]
        res.append(prev_interval)
        return res

        