
from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []
        current_time = 0

        for i, duration in enumerate(tasks):
            current_time = max(current_time, i)

            while busy and busy[0][0] <= current_time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            result.append(index)

            heapq.heappush(
                busy,
                (current_time + duration, weight, index)
            )

        return result
