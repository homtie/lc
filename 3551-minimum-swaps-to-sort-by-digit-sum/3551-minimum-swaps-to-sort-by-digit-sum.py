
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        arr = [(x, i) for i, x in enumerate(nums)]

        arr.sort(key=lambda p: (digit_sum(p[0]), p[0]))

        swaps = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i] or arr[i][1] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][1]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
