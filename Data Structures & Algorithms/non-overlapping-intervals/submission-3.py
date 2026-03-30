class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prevInterval=intervals[0]
        intervalsToRemove=0
        for currInterval in intervals[1:]:
            if currInterval[0]<prevInterval[1]:
                intervalsToRemove+=1
                prevInterval[1]=min(prevInterval[1],currInterval[1])
            else:
                prevInterval=currInterval
        return intervalsToRemove
                

        