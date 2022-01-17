"""
Problem: You are given an integer array 'nums' where the largest integer is unique.
    Determine whether the largest element in the array is at least twice as much as
    every other number in the array. If it is, returen the index of the largest element,
    or return -1 otherwise.
"""

class Solution:
    def dominantIndex(self, nums):
        
        len_list = len(nums)
              
        if len_list == 1:
            return 0

        max_val = max(nums)
        max_index = nums.index(max_val)
        
        for i in range(len_list):
            if i != max_index:           
                _twice = nums[i] * 2
                if _twice > max_val:
                    return -1
        
        return max_index