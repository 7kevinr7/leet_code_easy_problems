
from Easy.base_tester import BaseTester

class Solution:
    @staticmethod
    def maxProfit(prices: list) -> int:
        max_profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - buy_price > max_profit:
                max_profit = prices[i] - buy_price
            elif prices[i] < buy_price:
                buy_price = prices[i]

        return max_profit

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8]]
        outputs = [5, 0, 7]

        Tester.test_all(Solution.maxProfit, inputs, outputs)