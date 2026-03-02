'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

class Solution:
  from heapq import heapify, heappop
  def topKFrequent(self, nums, k):
      count = {}
      for n in nums:
          count[n] = count.get(n, 0) + 1
      
      maxHeap = [[-cnt, n] for n, cnt in count.items()]
      heapify(maxHeap)
      res = []
      while len(res) < k:
          cnt, n = heappop(maxHeap)
          res.append(n)
      return res
