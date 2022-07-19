class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        N = len(prices)
        pre_profit = [0] * N
        post_profit = [0] * (N+ 1)

        global_min = prices[0]
        max_profit = 0

        for i in range(1, N):
            cur_profit = prices[i] - global_min
            max_profit = max(max_profit, cur_profit)
            global_min = min(global_min, prices[i])
            pre_profit[i] = max_profit

        global_max = prices[N - 1]
        max_profit = 0

        for i in range(N - 2, -1, -1):
            global_max = max(global_max, prices[i])
            cur_profit = global_max - prices[i]
            max_profit = max(cur_profit, max_profit)
            post_profit[i] = max_profit

        max_res = 0
        for i in range(0, N):
            max_res = max(pre_profit[i] + post_profit[i + 1], max_res)

        return max_res


if __name__ == '__main__':
    h1 = [1,2,3,4,5]
    res = Solution().maxProfit(h1)
    print(res)
