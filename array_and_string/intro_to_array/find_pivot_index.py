"""
Problem: Given an array of integers nums, calculate the pivot index.

Pivot Index: Index where the sum of all the numbers strictly to the
    left of the index is equal to the sum of all the numbers strictly to the index's right

If the index is on the left edge the the array,
    then the left sum is 0 because tjere are no elements to the left.
    This also applies tot eh right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    def pivotIndex(self, nums):

        len_list = len(nums)
        sum_list = sum(nums) - nums[0]
        left_sum = 0

        if len_list == 1:        
            return 0

        if sum(nums[1:]) == 0:
            return 0
        
        for i in range(len_list - 1):
            left_sum += nums[i]
            sum_list -= nums[i + 1]
            if left_sum == sum_list:
                return i + 1

        if sum(nums[:-1]) == 0:
            return len_list - 1

        return -1