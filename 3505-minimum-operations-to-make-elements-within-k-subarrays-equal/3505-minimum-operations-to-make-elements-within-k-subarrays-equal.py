
import heapq
from collections import defaultdict
from typing import List


class DualHeap:
    def __init__(self):
        self.small = []
        self.large = []
        self.delayed = defaultdict(int)
        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap):
        while heap:
            x = -heap[0] if heap is self.small else heap[0]
            if self.delayed[x]:
                self.delayed[x] -= 1
                if self.delayed[x] == 0:
                    del self.delayed[x]
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            self.prune(self.small)
            x = -heapq.heappop(self.small)
            self.small_size -= 1
            self.small_sum -= x
            heapq.heappush(self.large, x)
            self.large_size += 1
            self.large_sum += x
            self.prune(self.small)

        elif self.small_size < self.large_size:
            self.prune(self.large)
            x = heapq.heappop(self.large)
            self.large_size -= 1
            self.large_sum -= x
            heapq.heappush(self.small, -x)
            self.small_size += 1
            self.small_sum += x
            self.prune(self.large)

    def add(self, x):
        self.prune(self.small)

        if not self.small or x <= -self.small[0]:
            heapq.heappush(self.small, -x)
            self.small_size += 1
            self.small_sum += x
        else:
            heapq.heappush(self.large, x)
            self.large_size += 1
            self.large_sum += x

        self.balance()

    def remove(self, x):
        self.prune(self.small)

        self.delayed[x] += 1

        if x <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= x
            if x == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.large_sum -= x
            if self.large and x == self.large[0]:
                self.prune(self.large)

        self.balance()

    def cost(self):
        self.prune(self.small)
        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        dh = DualHeap()

        for i in range(x):
            dh.add(nums[i])

        costs = [dh.cost()]

        for i in range(x, n):
            dh.remove(nums[i - x])
            dh.add(nums[i])
            costs.append(dh.cost())

        INF = 10**18
        dp = [INF] * (k + 1)
        dp[0] = 0

        for i, cost in enumerate(costs):
            for j in range(k, 0, -1):
                if i >= x - 1:
                    dp[j] = min(dp[j], dp[j - 1] + cost)

            # Ensure selected windows do not overlap.
            # Use a separate DP implementation below instead.

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0] = [0] * (n + 1)

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                dp[j][i] = dp[j][i - 1]

                if i >= x:
                    dp[j][i] = min(
                        dp[j][i],
                        dp[j - 1][i - x] + costs[i - x]
                    )

        return dp[k][n]
