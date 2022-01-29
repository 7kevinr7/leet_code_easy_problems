
from util.base_tester import BaseTester

class Solution:
    @staticmethod
    def disappeared_array(nums: list) -> list:
        return list(set(range(1, len(nums) + 1)).difference(nums))

class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1]]
        outputs = [[5, 6], [2]]

        return Tester.test_all(Solution.disappeared_array, inputs, outputs, verbose)