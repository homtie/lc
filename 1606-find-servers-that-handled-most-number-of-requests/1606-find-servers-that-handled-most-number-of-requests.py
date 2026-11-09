
from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        tree = [0] * (k + 1)

        def update(i, val):
            while i <= k:
                tree[i] += val
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        def find_kth(target):
            idx = 0
            bit = 1 << (k.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < target:
                    idx = nxt
                    target -= tree[nxt]
                bit >>= 1

            return idx + 1

        # Initially all servers are available.
        for i in range(1, k + 1):
            update(i, 1)

        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # Release servers that have finished.
            while busy and busy[0][0] <= start:
                finish, server = heapq.heappop(busy)
                update(server + 1, 1)

            available = query(k)

            if available == 0:
                continue

            # Find first available server >= i % k.
            start_server = i % k
            before = query(start_server)

            rank = before + 1

            if rank > available:
                rank = 1

            server = find_kth(rank) - 1

            # Mark server as busy.
            update(server + 1, -1)

            count[server] += 1

            heapq.heappush(
                busy,
                (start + duration, server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
