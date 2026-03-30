"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        prev_interval=intervals[0]
        for curr_interval in intervals[1:]:
            if curr_interval.start<prev_interval.end:
                return False
            else:
                prev_interval=curr_interval
        return True 
