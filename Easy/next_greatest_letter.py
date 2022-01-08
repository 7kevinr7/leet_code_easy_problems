
from Easy.base_tester import BaseTester

class Solution:

    @staticmethod
    def next_greatest_letter(nums: list, target: int) -> int:
        first = 0
        last = len(nums) - 1
        mid = int((first + last) / 2)

        while first < last:
            if ord(target) > ord(nums[mid]):
                first = mid + 1
            else:
                last = mid

            mid = int((first + last) / 2)

        if target >= nums[mid]:
            if mid + 1 >= len(nums):
                return nums[0]
            return nums[mid + 1]
        else:
            return nums[mid]

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"], ["c", "f", "j"]],
                  ["a", "c", "d", "g", "j"]]
        outputs = ["c", "f", "f", "j", "c"]

        Tester.test_all_multi_param(Solution.next_greatest_letter, inputs, outputs)
