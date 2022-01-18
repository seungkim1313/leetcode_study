"""
Problem: Given an 'm x n' matrix, return all elements of
    the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        result = []
        x = 0
        y = 0
        direction_x = 0
        direction_y = 1

        for steps in range(row * col):
            result.append(matrix[x][y])
            matrix[x][y] = ''
            if matrix[(x + direction_x)%row][(y + direction_y)%col] == '':   
                direction_x, direction_y = direction_y, -direction_x
            x = x + direction_x
            y = y + direction_y
        return result