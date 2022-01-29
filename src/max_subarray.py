
from util.base_tester import BaseTester


class Solution:
    @staticmethod
    def maxSubArray(nums: list) -> int:
        max_sum = nums[0]
        sum_to = list()

        for index in range(len(nums)):
            sum_to.append(sum(nums[0:index+1]))

        end_index = sum_to.index(max(sum_to))

        index = 0

        while index < len(nums) and index < end_index:
            if sum(nums[index:end_index+1]) > max_sum:
                max_sum = sum(nums[index:end_index+1])

            index += 1

        return max_sum

class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]
        outputs = [6, 1, 23]

        return Tester.test_all(Solution.maxSubArray, inputs, outputs, verbose)
