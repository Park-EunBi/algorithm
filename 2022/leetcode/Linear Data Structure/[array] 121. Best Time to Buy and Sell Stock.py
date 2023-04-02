from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0
print(s.maxProfit([2,4,1])) # 2
print(s.maxProfit([3,2,6,5,0,3])) # 4