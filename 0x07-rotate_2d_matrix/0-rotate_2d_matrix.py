#!/usr/bin/python3
"""Rotates a 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2D matrix clockwise by 90 degrees
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # Save top, left value
            topLeft = matrix[top][left + i]
            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # Move top left to top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
