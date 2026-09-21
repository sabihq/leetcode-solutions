class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy = float("-inf")
        first_sell = 0
        second_buy = float("-inf")
        second_sell = 0

        for price in prices:
            # Best balance after buying the first stock
            first_buy = max(first_buy, -price)

            # Best profit after selling the first stock
            first_sell = max(first_sell, first_buy + price)

            # Best balance after buying the second stock
            second_buy = max(second_buy, first_sell - price)

            # Best profit after selling the second stock
            second_sell = max(second_sell, second_buy + price)

        return second_sell