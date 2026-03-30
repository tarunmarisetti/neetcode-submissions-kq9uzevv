"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)-1):
            curr_interval=intervals[i+1]
            prev_interval=intervals[i]
            if curr_interval.start<prev_interval.end and curr_interval.end>prev_interval.start:
                return False
        return True

