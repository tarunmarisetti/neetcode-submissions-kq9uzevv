class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res=[]

        prevInterval=intervals[0]
        for currInterval in intervals[1:]:
            start,end=currInterval
            if start<=prevInterval[1]:
                prevInterval=[prevInterval[0], max(prevInterval[1],end)]
            else:
                res.append(prevInterval)
                prevInterval=currInterval
        res.append(prevInterval)
        return res
