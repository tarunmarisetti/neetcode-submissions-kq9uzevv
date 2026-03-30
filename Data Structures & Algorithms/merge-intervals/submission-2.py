class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        prevInterval=intervals[0]
        res=[]
        for currInterval in intervals[1:]:
            if currInterval[0]<=prevInterval[1]:
                prevInterval[1]=max(currInterval[1],prevInterval[1])
            else:
                res.append(prevInterval)
                prevInterval=currInterval
        res.append(prevInterval)
        return res
        