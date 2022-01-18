"""
Problem: Given an integer 'numRows', 
    return the first numRows of Pascal's Triangle.
    In Pascal's triangle, each number is the sum of two
    numbers directly above.
"""

class Solution:
    def generate(self, numRows):
        result = []
        for row in range(numRows):
            result.append([])
            result[row].append(1)
            for index in range(1, row):
                result[row].append(result[row-1][index-1]+result[row-1][index])
            if row != 0:
                result[row].append(1)
        return result