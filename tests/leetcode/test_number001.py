import unittest
from src.leetcode.number001 import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum_v1(self):
        self.assertEqual([0, 1], Solution.two_sum_v1([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
