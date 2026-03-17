'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''
class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
      stack = []
      for n in num:
          while stack and k > 0 and stack[-1] > n:
              stack.pop()
              k -= 1
          
          stack.append(n)
      
      if k:
          stack = stack[:len(stack) - k]
      
      return ''.join(stack).lstrip('0') or '0'



        
