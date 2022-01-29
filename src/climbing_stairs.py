
from util.base_tester import BaseTester

class Solution:
    @staticmethod
    def climbing_stairs(n: int) -> int:
        max_twos = int(n / 2)
        ways = 1

        for i in range(1, max_twos + 1):
            ways += n - i

        return ways

class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [2, 3, 4, 5]
        outputs = [2, 3, 6, 8]

        return Tester.test_all(Solution.climbing_stairs, inputs, outputs, verbose)
