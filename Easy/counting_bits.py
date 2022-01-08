
from Easy.base_tester import BaseTester

class Solution:

    @staticmethod
    def counting_bits(num: int) -> list:
        bit_list = list()
        index = 0

        while index <= num:
            bit_list.append(format(index, 'b').count('1'))
            index += 1

        return bit_list

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [2, 5]
        outputs = [[0, 1, 1], [0, 1, 1, 2, 1, 2]]

        Tester.test_all(Solution.counting_bits, inputs, outputs)
