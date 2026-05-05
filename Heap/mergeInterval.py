'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

class Solution:
  def merge(self, intervals: List[List[int]]):
      intervals.sort()
      merged = [intervals[0]]
      for interval in intervals[1:]:
          if interval[0] <= merged[-1][1]:
              merged[-1] = (min(interval[0], merged[-1][0]), max(interval[1], merged[-1][1]))
          else:
              merged.append(interval)
      
      return merged
      
