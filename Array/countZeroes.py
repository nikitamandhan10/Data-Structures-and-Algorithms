'''
Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

Examples:
Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
Output: 3
Explanation: There are 3 0's in the given array.
'''

class Solution:
    def countZeroes(self, arr):
        n = len(arr)
        left, right = 0, n - 1
        first_zero = n  # default if no 0 found

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == 0:
                first_zero = mid
                right = mid - 1  # search left side
            else:
                left = mid + 1

        return n - first_zero
