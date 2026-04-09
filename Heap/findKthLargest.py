'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
'''
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
      minHeap = []

      for n in nums:
          if minHeap and len(minHeap) >= k and n > minHeap[0]:
              heappop(minHeap)
          
          if len(minHeap) < k:
              heappush(minHeap, n)
      return minHeap[0]
