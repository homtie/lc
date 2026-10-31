
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        up = [0] * n

        for i in range(m):
            next_up = [0] * n
            left = 1 if i == 0 else 0

            for j in range(n):
                if i == m - 1 and j == n - 1:
                    return (left + up[j]) % MOD

                if grid[i][j] == 0:
                    ways = (left + up[j]) % MOD

                    left = ways
                    next_up[j] = ways

                else:
                    # Right-moving paths get redirected down.
                    next_up[j] = left

                    # Down-moving paths get redirected right.
                    left = up[j]

            up = next_up

        return 0
