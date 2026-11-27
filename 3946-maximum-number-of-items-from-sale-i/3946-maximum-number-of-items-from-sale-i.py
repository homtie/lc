
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cheapest = min(price for _, price in items)

        gains = []
        for i in range(n):
            f, p = items[i]
            free = sum(1 for j in range(n) if j != i and items[j][0] % f == 0)
            gains.append((p, free + 1))

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for price, gain in gains:
            for b in range(budget, price - 1, -1):
                if dp[b - price] != -1:
                    dp[b] = max(dp[b], dp[b - price] + gain)

        ans = 0
        for spent in range(budget + 1):
            if dp[spent] != -1:
                ans = max(ans, dp[spent] + (budget - spent) // cheapest)

        return ans
