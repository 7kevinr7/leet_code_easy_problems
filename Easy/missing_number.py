
from Easy.base_tester import BaseTester

class Solution:
    @staticmethod
    def missingNumber(nums: list) -> bool:
        return set(range(len(nums) + 1)).difference(nums).pop()

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [0]]
        outputs = [2, 2, 8, 1]

        Tester.test_all(Solution.missingNumber, inputs, outputs)