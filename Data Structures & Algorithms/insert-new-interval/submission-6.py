class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals :
            return [newInterval]
        
        # binary serach to find the index to insert the new interval
        left,right=0,len(intervals)-1
        target=newInterval[0]
        while left<=right:
            mid=(left+right)//2
            if intervals[mid][0]>target:
                right=mid-1
            else:
                left=mid+1
        intervals.insert(left, newInterval)
        print(intervals)

        res=[]
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1],interval[1])
        return res


        