import unittest
from src.leetcode.number001 import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum_v1(self):
        self.assertEqual([0, 1], Solution.two_sum_v1([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], Solution.two_sum_v1([3, 2, 4], 6))
        self.assertEqual([0, 1], Solution.two_sum_v1([3, 3], 6))

    def test_two_sum_v2(self):
        self.assertEqual([0, 1], Solution.two_sum_v2([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], Solution.two_sum_v2([3, 2, 4], 6))
        self.assertEqual([0, 1], Solution.two_sum_v2([3, 3], 6))

    def test_two_sum_v3(self):
        self.assertEqual([0, 1], Solution.two_sum_v3([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], Solution.two_sum_v3([3, 2, 4], 6))
        self.assertEqual([0, 1], Solution.two_sum_v3([3, 3], 6))


if __name__ == '__main__':
    unittest.main()
