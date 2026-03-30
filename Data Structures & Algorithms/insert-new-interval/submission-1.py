class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res=[]
        prev_interval=intervals[0]
        for curr_interval in intervals[1:]:
            if curr_interval[0]<=prev_interval[1]:
                prev_interval=[prev_interval[0],max(prev_interval[1],curr_interval[1])]
            else:
                res.append(prev_interval)
                prev_interval=curr_interval
        res.append(prev_interval)
        return res

        