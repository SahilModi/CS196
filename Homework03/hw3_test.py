import unittest

from hw3 import *


# test file for homework 3

# these are the student tests. the autograder tests will be considerably more rigorous

class tester(unittest.TestCase):
    def test_max_sum_subrectangle(self):
        self.assertEquals(max_sum_subrectangle([[1, 2], [3, 4]]), 10)
        self.assertEquals(max_sum_subrectangle([[1, 2], [-3, 0]]), 3)
        self.assertEquals(max_sum_subrectangle([[1, -2, 0], [-1, 3, 0], [3, -1, -9]]), 4)

    def test_max_sum_subarray(self):
        self.assertEquals(max_sum_subarray([1, 2, 3, 4, 5]), 15)
        self.assertEquals(max_sum_subarray([1, -3, 4, 1, -2, 3]), 6)
        self.assertEquals(max_sum_subarray([1, -3, 4, 1, -2, 1]), 5)
        self.assertEquals(max_sum_subarray([-1, -2, -3, -4, -5]), -1)

    def test_max_2d_array(self):
        self.assertEquals(max_2d_array([[4, 2], [3, -1]]), 4)
        self.assertEquals(max_2d_array([[-300, -200], [-300, -100]]), -100)

    def test_search_2d_array(self):
        self.assertEquals(search_2d_array([[1, 2, 3], [8, 11, 16], [23, 24, 25]], 8), [1, 0])
        self.assertEquals(search_2d_array([[1, 2, 3], [8, 11, 16], [23, 24, 25]], 20), None)

    def test_matrix_transpose(self):
        self.assertEquals(matrix_transpose([[1]]), [[1]])
        self.assertEquals(matrix_transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEquals(matrix_transpose([[1, 2], [3, 4], [5, 6], [7, 8]]), [[1, 3, 5, 7], [2, 4, 6, 8]])

    def test_binary_search(self):
        self.assertEquals(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEquals(binary_search([1, 2, 3, 4, 5], 0), None)
        self.assertEquals(binary_search([3, 8, 32, 43, 132, 1000], 132), 4)

    def test_max_array_flatten(self):
        self.assertEquals(max_array_flatten([1, 2, [3, 4], 5]), 1)
        self.assertEquals(max_array_flatten([1, 2, 3, 4, 5]), 0)
        self.assertEquals(max_array_flatten([[1, [2, 3], 4], [5], 6]), 2)


if __name__ == "__main__":
    unittest.main(module=__name__, buffer=True, exit=False)
