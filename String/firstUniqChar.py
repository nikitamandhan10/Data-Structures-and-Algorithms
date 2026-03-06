'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0
'''

class Solution:
  def firstUniqChar(self, s):
      count = {}
      for ch in s:
          count[ch] = count.get(ch, 0) + 1
      
      for i, ch in enumerate(s):
          if count[ch] == 1:
              return i
      return -1


