class Solution:
    def maxProfit(self, kk, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if kk == 0:
            return 0

        global_profit = [[0] * (kk + 1) for _ in range(len(prices) + 1)]
        local_profit = [[0] * (kk + 1) for _ in range(len(prices) + 1)]
        large_k = self.larger_k_condition(prices)

        global_profit[0][0] = 0
        local_profit[0][0] = 0

        for day_i in range(1, len(prices) + 1):
            global_profit[day_i][0] = 0
            local_profit[day_i][0] = 0

            for j in range(1, kk + 1):
                if j >= day_i - 1:
                    global_profit[day_i][j] = large_k[day_i - 1]
                    local_profit[day_i][j] = global_profit[day_i][j]
                else:

                    diff = None
                    if day_i == 1:
                        diff = 0
                    else:
                        diff = prices[day_i - 1] - prices[day_i - 2]

                    local_profit[day_i][j] = max(global_profit[day_i - 1][j - 1] + max(diff, 0),
                                                 local_profit[day_i - 1][j] + diff)

                    global_profit[day_i][j] = max(global_profit[day_i - 1][j],
                                                  local_profit[day_i][j])
        
        return global_profit[len(prices)][kk]

    def larger_k_condition(self, prices):
        auc = 0
        res = [0]
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                auc += prices[i] - prices[i - 1]
            res.append(auc)
        return res


if __name__ == '__main__':
    k = 2
    h1 = [2, 4, 1]

    print(Solution().maxProfit(k, h1))
