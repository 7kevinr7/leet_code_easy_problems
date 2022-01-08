
from Easy.base_tester import BaseTester

class Solution:

    @staticmethod
    def binary_search_recurse(nums: list, target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target

        if target < nums[int(len(nums) / 2)]:
            if Solution.binary_search_recurse(nums[0:int(len(nums) / 2)], target):
                return True
        elif Solution.binary_search_recurse(nums[int(len(nums) / 2 + 1):], target):
            return True

        return False

    @staticmethod
    def binary_search(nums: list, target: int) -> int:
        if Solution.binary_search_recurse(nums, target):
            return nums.index(target)
        else:
            return -1

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[[-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]], [9, 2]]
        outputs = [4, -1]

        Tester.test_all_multi_param(Solution.binary_search, inputs, outputs)
