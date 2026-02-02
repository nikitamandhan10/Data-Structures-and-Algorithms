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
