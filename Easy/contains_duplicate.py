
from Easy.base_tester import BaseTester
from collections import Counter

class Solution:

    @staticmethod
    def containsDuplicate(nums: list) -> bool:
        return any(count > 1 for count in Counter(nums).values())

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
        outputs = [True, False, True]

        Tester.test_all(Solution.containsDuplicate, inputs, outputs)
