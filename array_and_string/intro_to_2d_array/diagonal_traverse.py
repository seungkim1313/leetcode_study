"""
Problem: Given an mxn matrix 'mat', return an array of
    all the elements of the arrya in a diagonal order.
"""

class Solution:
    def findDiagonalOrder(self, mat):
        
        if len(mat) == 1:
            return mat[0]
        
        row = len(mat)
        col = len(mat[0])
        storage = []
        answer = []
        
        for i in range(row+col-1):
            storage.append([])
        for x in range(row):
            for y in range(col):
                _id = x+y
                storage[_id].append(mat[x][y])
        for i in range(len(storage)):
            if i % 2 == 1:
                answer.extend(storage[i])
            else:
                answer.extend(storage[i][::-1])
        return answer              