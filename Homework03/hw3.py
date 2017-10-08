##################################
#                                #
#  Homework 3                    #
#  Released: September 26, 2017  #
#  Due: October 10, 2017         #
#                                #
##################################


# Matrix Transpose
# 
# Description:
#     Given an m x n matrix A, return A^T, that is, 
#     return the transpose of the matrix A.
# 
# Example(s):
# 
#     Example 1:
#         Input:
#             A = [[1]]
#         Output:
#             [[1]]
# 
#     Example 2:
#         Input:
#             A = [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]
#         Output:
#             [[1, 4, 7],
#              [2, 5, 8],
#              [3, 6, 9]]
#

def matrix_transpose(A):
    a2 = [[0 for x in range(len(A))] for y in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            a2[j][i] = A[i][j]
    return a2


# Max Element in 2-D Array
# 
# Description:
#     Given a 2-d array grid of integers, 
#     determine the maximum number in grid.
# 
# Example(s):
#     Example 1:
#         Input:
#             grid = [[4, 2],
#                     [3, -1]]
#         Output:
#             4
#     
#     Example 2:
#         Input:
#             grid = [[-300, -200],
#                     [-300, -100]]
#         Output:
#             -100
# 
def max_2d_array(grid):
    max = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] > max):
                max = grid[i][j]
    # print(max)
    return max


# Binary Search
# 
# Description:
#     Given a sorted (increasing) array with distinct integers and a
#     target integer, determine the index of target in the given array. 
#     If target is not in the array, return None. Try to use the fact
#     that the array is sorted to optimize your algorithm.
# 
# Example(s):
# 
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 3
#         Output:
#             2
# 
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 0
#         Output:
#             None
# 
def binary_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return None


# Sorted Matrix Search
# 
# Description:
#     Given a square 2d array of integers and a target integer 
#     return the coordinates of the target integer as a tuple
#     in the form (row, col) if the element exists in the matrix, 
#     or None if the element does not exists. The 2d array 
#     is guaranteed to be sorted ascending row-wise, 
#     and the zeroth element of each row is strictly larger than 
#     the last element of the previous row.
# 
# Example(s):
#     Example 1:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 8
#         Output:
#             (1, 0)
# 
#     Example 2:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 20
#         Output:
#             None
# 
def search_2d_array(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == target):
                list = [i, j]
                return list
    return None


# Maximum Sum Subarray
# 
# Description:
#     Given an array of integers, determine the maximum sum of
#     a continuous subarray of the given array.
# 
# Examples(s):
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Ouput:
#             15
# 
#     Example 2:
#         Input:
#             arr = [1, -3, 4, 1, -2, 3]
#         Output:
#             6
# 
def max_sum_subarray(arr):
    result = arr[0]
    temp = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):  # subarray
            temp += arr[j]
            if temp > result:
                result = temp
        temp = 0
    return result


# Maximum Sum Sub-Rectangle
# 
# Description:
#     Given a 2-d array of integers, determine the
#     maximum sub-rectangle sum.
# 
# Example(s):
#     Example 1:
#         Input:
#             grid = [[1, 2],
#                     [3, 4]]
#         Output:
#             10
# 
#     Example 2:
#         Input:
#             grid = [[1,  2],
#                     [-3, 0]]
#         Ouput:
#             3
# 
#     Example 3:
#         Input:
#             grid = [[ 1, -2,  0],
#                     [-1,  3,  0],
#                     [ 3, -1, -9]]
#         Output:
#             4
# 
def max_sum_subrectangle(grid):
    result = grid[0][0] + grid[0][1]
    for r in range(len(grid) - 1):
        for c in range(len(grid[0]) - 1):
            if grid[r][c] + grid[r][c + 1] > result: result = grid[r][c] + grid[r][c + 1]
            if grid[r][c] + grid[r + 1][c] > result: result = grid[r][c] + grid[r - 1][c]
            if grid[r][c] + grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 1][c] > result:
                result = grid[r][c] + grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 1][c]
    return result


# Maximum Number of Times an Array can be Flattened
# 
# Description:
#     Given an array of integers and arrays, 
#     return the maximum number of times arr can be flattened. 
#     For example, if arr = [1, 2, [3, 4], 5], 
#     then arr could be flattened once.
# 
# Example(s):
#     Example 1:
#         Input:
#             arr = [1, 2, [3, 4], 5]
#         Output:
#             1
# 
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Output:
#             0
# 
def max_array_flatten(arr):
    result = 0
    for r in range(len(arr)):
        if isinstance(arr[r], list):
            result += 1

    return result
