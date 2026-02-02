def subarraySum(self, nums: List[int], k: int) -> int:
  prefix = {0 : 1}
  curr = res = 0
  for n in nums:
      curr += n
      if curr - k in prefix:
          res += prefix[curr - k]
  
      prefix[curr] = prefix.get(curr, 0) + 1
  return res
      
