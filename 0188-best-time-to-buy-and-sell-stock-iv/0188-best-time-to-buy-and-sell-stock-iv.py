class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n <= 1:
            return 0

        # If k is large, we can treat it as unlimited transactions.
        if k >= n // 2:
            profit = 0

            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        # buy[t] = best balance after buying transaction t
        # sell[t] = best profit after selling transaction t
        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for transaction in range(1, k + 1):
                buy[transaction] = max(
                    buy[transaction],
                    sell[transaction - 1] - price
                )

                sell[transaction] = max(
                    sell[transaction],
                    buy[transaction] + price
                )

        return sell[k]