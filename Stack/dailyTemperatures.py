'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

'''

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
  stack = []
  res = [0] * len(temperatures)
  for i, t in enumerate(temperatures):
      while stack and stack[-1][0] < t:
          res[stack[-1][1]] = i - stack[-1][1]
          stack.pop()

      stack.append([t, i])
  return res
