'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

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
