
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # State: (node, consecutive_count)
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            cost, u, count = heapq.heappop(heap)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(
                        heap, (new_cost, v, new_count)
                    )

        return -1
