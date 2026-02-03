'''
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
'''
def customSortString(self, order, s):
  sCount = {}
  for ch in s:
      sCount[ch] = sCount.get(ch, 0) + 1
  
  res = ""
  for c in order:
      if c in sCount:
          res += c * sCount[c]
          del sCount[c]
  for ch, cnt in sCount.items():
      res += ch * cnt
  return res
