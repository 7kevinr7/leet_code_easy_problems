

class Solution:

    def __init__(self):
        self.numArray = None

    class NumArray:
        def __init__(self, nums: list):
            self.nums = nums

        def sumRange(self, left: int, right: int) -> int:
            return sum(self.nums[left:right+1])

    def sum_query(self, queries: any, nums: list) -> list:
        if queries == "NumArray":
            self.numArray = Solution.NumArray(nums)
            return None
        elif queries == "sumRange":
            return self.numArray.sumRange(nums[0], nums[1])

class Tester:

    @staticmethod
    def test():
        inputs = [["NumArray", "sumRange", "sumRange", "sumRange"],
                  [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]]
        outputs = [None, 1, -1, -3]

        solution = Solution()

        for index in range(len(inputs[0])):
            result = solution.sum_query(inputs[0][index], inputs[1][index])
            print(f"Test {index + 1} - {inputs[0][index], inputs[1][index]}: {outputs[index]} -> {result}")
            assert outputs[index] == result