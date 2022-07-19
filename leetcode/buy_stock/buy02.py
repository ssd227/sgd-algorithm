class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        auc = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] >0:
                auc += prices[i]-prices[i-1]

        return auc



if __name__ == '__main__':
    h1 = [7, 1, 5, 3, 6, 4]
    res = Solution().maxProfit(h1)
    print(res)
