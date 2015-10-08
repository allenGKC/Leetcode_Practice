'''
Problem:Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length <= 1:
            return intervals
        result = []
        for i in sorted(intervals,key=lambda i:i.start):
            if result and i.start<=result[-1].end:
                result[-1].end = max(result[-1].end,i.end)
            else:
                result.append(i)
        return result
        

'''
Test Case:
'''
if __name__ == '__main__':
    