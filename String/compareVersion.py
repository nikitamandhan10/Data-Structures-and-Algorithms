'''
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. 
The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
'''

class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
      v1 = version1.split('.')
      v2 = version2.split('.')

      for i in range(max(len(v1), len(v2))):
          n1 = int(v1[i]) if i < len(v1) else 0
          n2 = int(v2[i]) if i < len(v2) else 0

          if n1 < n2:
              return -1
          elif n1 > n2:
              return 1
      return 0


