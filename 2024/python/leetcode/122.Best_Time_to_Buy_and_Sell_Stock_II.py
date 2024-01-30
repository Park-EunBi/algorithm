class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sol_1
        ret = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                ret += prices[i + 1] - prices[i]
        return ret

        # sol_2
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))