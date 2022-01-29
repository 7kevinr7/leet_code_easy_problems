
from util.base_tester import BaseTester


class Solution:

    @staticmethod
    def peak_index_mt_array_n_time(arr: list) -> int:
        peak = arr[0]
        peak_index = 0

        while peak < arr[peak_index + 1]:
            peak = arr[peak_index + 1]
            peak_index += 1

        return peak_index


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[0, 1, 0], [0, 2, 1, 0], [0, 10, 5, 2]]
        outputs = [1, 1, 1]

        return Tester.test_all(Solution.peak_index_mt_array_n_time, inputs, outputs, verbose)
