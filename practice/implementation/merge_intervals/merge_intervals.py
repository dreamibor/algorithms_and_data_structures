"""
Merge Intervals - Merge Intervals (medium)

Description:
Given a list of intervals, merge all the overlapping intervals to produce a list that has only 
mutually exclusive intervals.

Example:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

LeetCode Link: https://leetcode-cn.com/problems/merge-intervals/
"""


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return "[" + str(self.start) + ", " + str(self.end) + "]"

def merge_intervals(intervals):
    """
    Assuming a.start <= b.start, then there are four possible scenarios:
        1. a and b do not overlap;
        2. some part of b overlaps with a;
        3. a fully overlaps b;
        4. b fully overlaps a but have same start time.
    
    Our goal is to merge the intervals whenever they overlap. For overlapping scenarios (2,3 and 
    4), we can merge them by: setting the new interval's start as a.start and setting the new 
    interval's end as the maximum of a.end or b.end.

    The final algorithm will be:

        1. Sort the intervals on the start time to ensure a.start <= b.start
        2. If ‘a’ overlaps ‘b’ (i.e. b.start <= a.end), we need to merge them into a new interval
        ‘c’ such that: 
            c.start = a.start
            c.end = max(a.end, b.end)
        3. keep repeating the above two steps to merge ‘c’ with the next interval if it overlaps 
        with ‘c’.
    """
    # Return the input since there are less than 2 intervals.
    if len(intervals) < 2: return intervals

    # Sort the intervals based on the start
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        # Overlapping intervals, adjust the 'end'
        if interval.start <= end:
            end = max(interval.end, end)
        # Non-overlapping interval, add the previous internval and reset
        # the start and end.
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
    
    # Add the last interval
    merged_intervals.append(Interval(start, end))

    return merged_intervals


if __name__ == "__main__":
    for i in merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        print(i)
    
    for i in merge_intervals([Interval(1, 5), Interval(2, 7), Interval(7, 9)]):
        print(i)