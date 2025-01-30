
from sol.x252 import Solution 
from typing import List

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Test case
solution = Solution()
intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

# Check if the result matches the expected output
assert solution.canAttendMeetings(intervals) == False

# Additional test case with overlapping intervals
intervals = [Interval(0, 30), Interval(20, 50), Interval(15, 25)]
assert solution.canAttendMeetings(intervals) == False

# Additional test case with no overlapping intervals
intervals = [Interval(0, 30), Interval(30, 50), Interval(50, 60)]
assert solution.canAttendMeetings(intervals) == True

