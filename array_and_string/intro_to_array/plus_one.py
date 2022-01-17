"""
Problem: You are given a large integer represented as an integer array digits,
    where each digits[i] is the i-th digit of the integer. The digits are
    ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits):
        
        digit_string = [str(digit) for digit in digits]
        digit_string = "".join(digit_string)
        digit_integer = int(digit_string) + 1
        
        digit_string = str(digit_integer)
        digit_map = map(int, digit_string)
        digit_list = list(digit_map)
        
        return digit_list