
from typing import List
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            ways = comb(len(arr) - 1, len(left))
            ways = ways * dfs(left) % MOD
            ways = ways * dfs(right) % MOD

            return ways

        return (dfs(nums) - 1) % MOD
