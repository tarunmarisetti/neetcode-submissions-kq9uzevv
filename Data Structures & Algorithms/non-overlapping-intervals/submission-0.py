class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # as they asked for minimum intervals to delete,
        # if we get an overlapping iterval we should delete the larger interval so leaves more space for future intervals.

        intervals.sort(key=lambda x:x[0])
        res=0
        prev_interval=intervals[0]
        for curr_interval in (intervals[1:]):
            if curr_interval[0]>=prev_interval[1]:
                prev_interval=curr_interval
            else:
                res+=1
                prev_interval=[prev_interval[0],min(prev_interval[1], curr_interval[1])]
        return res  

        
        