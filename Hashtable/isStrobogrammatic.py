'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Input: num = "69"
Output: true
'''

class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
      stroboMap = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9': '6'}
      
      i , j = 0, len(num) - 1
      while i <= j:
          if num[i] not in stroboMap or stroboMap[num[i]] != num[j]:
              return False
          i += 1
          j -= 1
      return True
