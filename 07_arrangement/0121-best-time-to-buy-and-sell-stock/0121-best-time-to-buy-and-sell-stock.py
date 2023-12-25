class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mp = 0

        for n in range(1, len(prices)):
            mn = min(mn, prices[n])
            mp = max(mp, prices[n] - mn)

        return mp