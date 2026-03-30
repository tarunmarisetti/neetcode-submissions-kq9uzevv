class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_interval=intervals[0]
        count=0
        for start,end in intervals[1:]:
            if start>=prev_interval[1]:
                prev_interval=[start,end]
            else:
                count+=1
                prev_interval=[prev_interval[0],min(end,prev_interval[1])]
        return count
        
        