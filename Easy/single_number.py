
from Easy.base_tester import BaseTester
from collections import Counter

class Solution:
    @staticmethod
    def single_number(nums: list) -> list:
        return Counter(nums).most_common()[::-1][0][0]

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
        outputs = [1, 4, 1]

        Tester.test_all(Solution.single_number, inputs, outputs)
