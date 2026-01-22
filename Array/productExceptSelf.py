def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0]*len(nums)
        temp = 1
        res = 1
        for i in range(len(nums)):
            res *= temp
            result[i] = res
            temp = nums[i]

        res = 1
        temp = 1
        for j in range(len(nums)-1,-1,-1):
            res*=temp
            result[j] = result[j]*res
            temp = nums[j]

        return result        