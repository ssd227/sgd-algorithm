class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        global_min = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            cur_profit = prices[i]-global_min
            max_profit = max(max_profit, cur_profit)
            global_min = min(global_min,prices[i])

        return max_profit


if __name__ == '__main__':
    price = [7, 1, 5, 3, 6, 4]
    res = Solution().maxProfit(price)
    print(res)
