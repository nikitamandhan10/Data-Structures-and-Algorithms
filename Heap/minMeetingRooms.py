'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
'''
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      intervals.sort()
      endTime = [intervals[0][1]]
      for interval in intervals[1:]:
          if interval[0] >= endTime[0]:
              heappop(endTime)
          heappush(endTime, interval[1])
      
      return len(endTime)
